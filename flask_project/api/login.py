from flask import render_template, redirect, request, flash
from werkzeug.security import generate_password_hash
import mysql.connector
from mysql.connector import Error
from app import app, db_manager
from werkzeug.security import check_password_hash


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Retrieve user data by username
        select_query = "SELECT * FROM Users WHERE username = %s"

        user_data = db_manager.fetchone(select_query, (username,))
        if user_data:
            # Verify the password using check_password_hash
            # Assuming password is in the fourth column
            stored_password = user_data[3]
            if check_password_hash(stored_password, password):
                # Log in the user (you can implement your login logic here)
                flash('Login successful', 'success')
                return redirect('/')
            else:
                flash('Incorrect password', 'error')
        else:
            flash('User not found', 'error')

    return render_template('login.html')
