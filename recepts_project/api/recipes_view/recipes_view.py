from flask import render_template, session, redirect, url_for
from app import app, db_manager
from tools.auth import login_required


@app.route('/recipe/<int:recipe_id>', methods=['GET'])
@login_required
def view_recipe(recipe_id):
    # Retrieve the recipe details from the database based on recipe_id
    select_recipe_query = f"""SELECT * FROM recipes WHERE id={recipe_id}"""
    recipe_data = db_manager.fetchone(select_recipe_query)
    if recipe_data:
        # Retrieve the username of the recipe creator
        select_user_query = f"SELECT first_name FROM Users WHERE id={recipe_data[-1]}"
        creator_name = db_manager.fetchone(select_user_query)[0]
        recipe_data_dict = {
            "description": recipe_data[2],
            "instructions": recipe_data[3],
            "date_made": recipe_data[4],
            "username": creator_name,
            "under_half_hour": recipe_data[5]

        }
        return render_template('view_recipes.html',
                               recipe=recipe_data_dict,
                               username=creator_name)
    else:
        return "Recipe not found", 404
