from flask import render_template, redirect, request, flash, session
from werkzeug.security import check_password_hash

from app import app, db_manager


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Retrieve user data by email
        select_query = "SELECT * FROM Users WHERE email=%s"

        user_data = db_manager.fetchone(select_query, (email,))
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
                return redirect('/')
            else:
                flash('Incorrect password', 'error')
        else:
            flash('User not found', 'error')

    return render_template('login.html')
