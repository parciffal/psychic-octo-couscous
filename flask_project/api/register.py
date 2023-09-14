from flask import render_template, redirect, request, url_for, flash
from werkzeug.security import generate_password_hash
import mysql.connector
from app import app, db_manager


# Replace with your MySQL database connection details

@app.route('/register', methods=['GET', 'POST'])
def show():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm-password']

        if username and email and password and confirm_password:
            if password == confirm_password:
                hashed_password = generate_password_hash(
                    password, method='sha256')

                # Check if the username or email already exists
                check_query = "SELECT * FROM Users WHERE username = %s OR email = %s"
                existing_user = db_manager.fetchone(
                    check_query, (username, email))

                if existing_user:
                    flash('Username or email already exists.', 'error')
                    return redirect('/register')

                # Insert the new user into the Users table
                insert_query = "INSERT INTO Users (username, email, password) VALUES (%s, %s, %s)"
                db_manager.query(
                    insert_query, (username, email, hashed_password))
                flash('Account created successfully. You can now log in.', 'success')
                return redirect('/login')

        flash('Missing fields or passwords do not match.', 'error')
    else:
        return render_template('register.html')
