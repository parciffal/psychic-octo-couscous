import re
from flask import render_template, request, session, redirect, url_for
from app import app, db_manager
from tools.auth import login_required
# Assume 'recipes' is a list of dictionaries representing recipe data
# Each dictionary in 'recipes' should have keys like 'id', 'name', 'user_id', etc.


@app.route('/recipes', methods=['GET'])
@login_required
def recipes():
    current_user_id = session['user_id']
    select_recipes_query = f"""SELECT * FROM recipes;"""
    data = db_manager.fetchall(select_recipes_query)
    recipes_data = []
    if data:
        for i in data:
            recipes_data.append({
                'id': i[0],
                'name': i[1],
                'user_id': i[2]
            })
    # recipes_data = [ {'id': i[0], 'name': i[1], 'user_id': i[2]} for i in data id data]
    print(recipes_data)

    return render_template('recipes.html', recipes=recipes_data, current_user_id=current_user_id)


@app.route("/recipes/new", methods=['GET', 'POST'])
@login_required
def new_recipes():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        instruction = request.form['instructions']
        date_made = request.form['date_made']
        under_half_hour = bool(request.form.get('under_half_hour'))

        insert_query = f"""
            INSERT recipes (name, description, instruction, date_made, under_half_hour)
            VALUES ('{name}', '{description}', '{instruction}', '{date_made}', {under_half_hour})
        """
        db_manager.query(insert_query)

        return redirect(url_for('recipes'))
    else:
        return render_template('new_recipes.html')
