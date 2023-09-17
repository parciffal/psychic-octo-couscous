from functools import wraps
from flask import redirect, session
from app import db_manager


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        """
        Decorator to check if a user is logged in.

        Args:
            f (function): The function to be decorated.

        Returns:
            function: The decorated function.
        """
        log_check_query = f"""SELECT is_logged FROM users WHERE email='{session.get("email")}';"""
        is_logged = db_manager.fetchone(log_check_query)
        if not is_logged:
            if 'email' not in session or 'user_id' not in session:
                return redirect('/login')
        return f(*args, **kwargs)
    return decorated_function
