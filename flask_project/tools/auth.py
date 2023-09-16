from functools import wraps
from flask import redirect, session
from app import db_manager
# Assuming you have a `current_user` object that represents the logged-in user
# You can replace this with your actual user management logic

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            # is_logged = db_manager.fetchone(f"""SELECT is_logged FROM users WHERE username='{session.get("username")}'""")
            # if not is_logged:
            user = "edgar"
            kwargs['user'] = user
            return redirect('/login')
        return f(*args, **kwargs)
    return decorated_function
