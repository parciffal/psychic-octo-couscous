from flask import render_template, redirect, request, url_for, flash
from werkzeug.security import generate_password_hash
from app import app, db_manager


def check_fields(first_name, last_name, email, password, confirm_password):
    check_pass = True
    if not first_name:
        check_pass = False
        flash('First name is empty', 'error')
    if not last_name:
        check_pass = False
        flash('Last name is empty', 'error')
    if not email:
        check_pass = False
        flash('Email is empty', 'error')
    if not password:
        check_pass = False
        flash('Password is empty', 'error')
    if not confirm_password:
        check_pass = False
        flash('Confirm Password is empty', 'error')
    if len(first_name) < 2:
        check_pass = False
        flash("First name can't be less then 2 characters", "error")
    if len(last_name) < 2:
        check_pass = False
        flash("Last name can't be less then 2 characters", "error")
    return check_pass
# Replace with your MySQL database connection details


@app.route('/register', methods=['GET', 'POST'])
def show():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm-password']
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
                    return redirect('/register')

                # Insert the new user into the Users table
                insert_query = "INSERT INTO Users (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)"
                db_manager.query(
                    insert_query, (first_name, last_name, email, hashed_password))
                flash('Account created successfully. You can now log in.', 'success')
                return redirect('/login')
        else:
            flash('Missing fields or passwords do not match.', 'error')
    else:
        return render_template('register.html')
