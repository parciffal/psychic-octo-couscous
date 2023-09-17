from app import app, db_manager
from flask import session, url_for, redirect
from tools.auth import login_required


@app.route('/recipes/delete/<int:recipe_id>', methods=['GET'])
@login_required
def delete_recipe(recipe_id):
    """
    Delete a recipe from the database.

    Requires the user to be logged in (authenticated through @login_required decorator).

    Args:
        recipe_id (int): The ID of the recipe to be deleted.

    Returns:
        Response: A Flask Response object for redirecting to the recipes page after deletion.
    """
    user_id = session['user_id']
    owner_id_query = f"""SELECT user_id FROM recipes WHERE id={recipe_id}"""
    owner_id = db_manager.fetchone(owner_id_query)
    owner_id = owner_id[0] if owner_id else None
    # Delete the recipe
    if owner_id == user_id:
        delete_recipe_query = f"DELETE FROM recipes WHERE id={recipe_id};"
        db_manager.query(delete_recipe_query)
    else:
        return
    # Redirect back to the recipes page after deletion
    return redirect(url_for('recipes'))
