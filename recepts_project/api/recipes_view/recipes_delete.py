from app import app, db_manager
from flask import session, request, url_for, redirect
from tools.auth import login_required


@app.route('/delete/<int:recipe_id>', methods=['GET'])
@login_required
def delete_recipe(recipe_id):
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
