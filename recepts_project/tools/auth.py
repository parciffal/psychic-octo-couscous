from functools import wraps
from flask import redirect, session
from app import db_manager
# Assuming you have a `current_user` object that represents the logged-in user
# You can replace this with your actual user management logic


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        log_check_query = f"""SELECT is_logged FROM users WHERE email='{session.get("email")}';"""
        is_logged = db_manager.fetchone(log_check_query)
        if not is_logged:
            if 'email' not in session or 'user_id' not in session:
                return redirect('/login')
        return f(*args, **kwargs)
    return decorated_function
