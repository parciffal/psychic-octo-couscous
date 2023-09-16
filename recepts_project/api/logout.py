from flask import redirect, url_for, session
from tools.auth import login_required
from app import app, db_manager


@app.route('/logout')
@login_required
def logout():
    login_query = f"""UPDATE Users SET is_logged=False WHERE id={session['user_id']}"""
    db_manager.query(login_query)
    session.pop('email', None)
    return redirect(url_for('login'))
