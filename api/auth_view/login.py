from flask import render_template, redirect, request, flash, session
from werkzeug.security import check_password_hash, generate_password_hash
import re
from app import app, db_manager

import re


def check_fields(first_name, last_name, email, password, confirm_password):
    """
    Check the validity of user registration fields and display flash messages for errors.

    Args:
        first_name (str): The user's first name.
        last_name (str): The user's last name.
        email (str): The user's email address.
        password (str): The user's password.
        confirm_password (str): The confirmation of the user's password.

    Returns:
        bool: True if all fields are valid, False otherwise.
    """

    check_pass = True
    email_format_valid = re.match(r"[^@]+@[^@]+\.[^@]+", email)

    if not first_name:
        check_pass = False
        flash('First name is empty', 'error')
    if not last_name:
        check_pass = False
        flash('Last name is empty', 'error')

    if not email:
        check_pass = False
        flash('Email is empty', 'error')

    elif not email_format_valid:
        check_pass = False
        flash('Email has an invalid format', 'error')

    if not password:
        check_pass = False
        flash('Password is empty', 'error')
    if not confirm_password:
        check_pass = False
        flash('Confirm Password is empty', 'error')
    if len(first_name) < 2:
        check_pass = False
        flash("First name can't be less than 2 characters", "error")
    if len(last_name) < 2:
        check_pass = False
        flash("Last name can't be less than 2 characters", "error")
    return check_pass


@app.route('/', methods=['GET', 'POST'])
def auth():
    """
    Handle user authentication and registration.

    GET: If the user is already logged in, redirect to '/recipes'.
    POST: Handle login and registration forms.

    Returns:
        Response: A Flask Response object (rendered template or redirect).
    """
    
    if request.method == 'POST':
        print(request.form.keys())
        if 'login-email' in request.form.keys():
            email = request.form['login-email']
            password = request.form['login-password']

            # Retrieve user data by email
            select_query = "SELECT * FROM Users WHERE email=%s"

            user_data = db_manager.fetchone(select_query, (email,))
            print("user", user_data)
            if user_data:
                # Verify the password using check_password_hash
                # Assuming password is in the fourth column
                stored_password = user_data[4]
                if check_password_hash(stored_password, password):
                    session['email'] = user_data[3]
                    session['user_id'] = user_data[0]
                    login_query = f"""UPDATE Users SET is_logged=True WHERE id={user_data[0]}"""
                    db_manager.query(login_query)
                    # Log in the user (you can implement your login logic here)
                    flash('Login successful', 'success')
                    return redirect('/recipes')
                else:
                    flash('Incorrect password', 'error')
            else:
                flash('User not found', 'error')

        elif 'registration-email' in request.form.keys():
            first_name = request.form['registration-first_name']
            last_name = request.form['registration-last_name']
            email = request.form['registration-email']
            password = request.form['registration-password']
            confirm_password = request.form['registration-confirm-password']
            if check_fields(first_name, last_name, email, password, confirm_password):
                if password == confirm_password:
                    hashed_password = generate_password_hash(
                        password, method='sha256')

                    # Check if the username or email already exists
                    check_query = "SELECT * FROM Users WHERE email=%s"
                    existing_user = db_manager.fetchone(
                        check_query, (email))

                    if existing_user:
                        flash('Email already exists.', 'error')
                        return redirect('/')

                    # Insert the new user into the Users table
                    insert_query = "INSERT INTO Users (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)"
                    db_manager.query(
                        insert_query, (first_name, last_name, email, hashed_password))
                    flash(
                        'Account created successfully. You can now log in.', 'success')
                    return redirect('/')
            else:
                flash('Missing fields or passwords do not match.', 'error')
    elif request.method == 'GET':
        if session.get('user_id'):
            return redirect('/recipes')

    return render_template('login.html')
