from flask import redirect, url_for, session
from tools.auth import login_required
from app import app


@app.route('/logout')
@login_required
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))
