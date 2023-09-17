import re
from flask import render_template, request, session, redirect, url_for
from app import app, db_manager
from tools.auth import login_required
# Assume 'recipes' is a list of dictionaries representing recipe data
# Each dictionary in 'recipes' should have keys like 'id', 'name', 'user_id', etc.

@app.route("/recipes/new", methods=['GET', 'POST'])
@login_required
def new_recipes():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        instruction = request.form['instructions']
        date_made = request.form['date_made']
        under_half_hour = bool(request.form.get('under_half_hour'))
        user_id = session['user_id']
        insert_query = f"""
            INSERT recipes (name, description, instruction, date_made, under_half_hour, user_id)
            VALUES ('{name}', '{description}', '{instruction}', '{date_made}', {under_half_hour}, {user_id})
        """
        db_manager.query(insert_query)

        return redirect(url_for('recipes'))
    else:
        return render_template('new_recipes.html')
