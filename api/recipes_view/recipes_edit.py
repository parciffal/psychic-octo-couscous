from flask import request
from flask import render_template, session, redirect, url_for
from app import app, db_manager
from tools.auth import login_required


@app.route('/recipes/edit/<int:recipe_id>', methods=['GET', 'POST'])
@login_required
def edit_recipe(recipe_id):
    """
    Edit a recipe by updating its details.

    If the request method is GET, retrieve the existing recipe data and render the edit form.
    If the request method is POST, update the recipe in the database with the new details.

    Args:
        recipe_id (int): The ID of the recipe to be edited.

    Returns:
        Response: A Flask Response object for rendering the edit form or redirecting to the recipes page after editing.
    """
    if request.method == 'GET':
        creator_name_query = f"""SELECT first_name FROM Users WHERE id={session['user_id']}"""
        creator_name = db_manager.fetchone(creator_name_query)
        # Retrieve the existing recipe data
        select_recipe_query = f"SELECT * FROM recipes WHERE id={recipe_id};"
        recipe_data = db_manager.fetchone(select_recipe_query)
        recipe_data_dict = {
            "id": recipe_data[0],
            "name": recipe_data[1],
            "description": recipe_data[2],
            "instructions": recipe_data[3],
            "date_made": recipe_data[4],
            "creator_name": creator_name,
            "under_half_hour": recipe_data[5]
        }
        if recipe_data:
            return render_template('edit_recipe.html', recipe=recipe_data_dict)
        else:
            # Handle the case where the recipe with the given ID does not exist
            return "Recipe not found", 404

    elif request.method == 'POST':
        # Handle the form submission to update the recipe
        new_name = request.form.get('name')
        new_description = request.form.get('description')
        new_instructions = request.form.get('instructions')
        new_date_made = request.form.get('date_made')
        new_under_half_hour = bool(request.form.get('under_half_hour'))

        # Update the recipe in the database
        update_recipe_query = f"""UPDATE recipes SET name='{new_name}', description='{new_description}', instruction='{new_instructions}', date_made='{new_date_made}', under_half_hour={int(new_under_half_hour)} WHERE id={recipe_id};"""
        print(update_recipe_query)
        db_manager.query(update_recipe_query)

        # Redirect back to the recipes page after editing
        return redirect(url_for('recipes'))
