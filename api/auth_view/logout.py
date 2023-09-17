from flask import redirect, session
from tools.auth import login_required
from app import app, db_manager


@app.route('/logout')
@login_required
def logout():
    """
    Log out the user by updating the 'is_logged' status in the database and clearing session data.

    Requires the user to be logged in (authenticated through @login_required decorator).

    Redirects the user to the home page after logging out.

    Returns:
        Response: A Flask Response object for redirecting to the home page.
    """

    login_query = f"""UPDATE Users SET is_logged=False WHERE id={session['user_id']}"""
    db_manager.query(login_query)
    session.pop('email', None)
    session.pop("user_id", None)
    return redirect('/')
