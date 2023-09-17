from flask import render_template, session, redirect, url_for
from app import app, db_manager
from tools.auth import login_required


@app.route('/recipes', methods=['GET'])
@app.route('/', methods=['GET'])
@login_required
def recipes():

    current_user_id = session['user_id']
    select_user_query = f"""SELECT first_name FROM Users WHERE id={current_user_id}"""
    current_user_name = db_manager.fetchone(select_user_query)
    select_recipes_query = f"""SELECT id, name, under_half_hour, user_id FROM recipes;"""
    data = db_manager.fetchall(select_recipes_query)
    recipes_data = []
    if data:
        for i in data:
            select_user_query = f"""SELECT first_name FROM Users WHERE id={i[2]}"""
            first_name = db_manager.fetchone(select_user_query)
            first_name = ("edgar",)
            recipes_data.append({
                'id': i[0],
                'name': i[1],
                'user_id': i[3],
                "under": i[2],
                "username": first_name[0]
            })

    return render_template('recipes.html',
                           recipes=recipes_data,
                           current_user_id=current_user_id,
                           current_user_name=current_user_name[0])
