from app import app, db_manager
from flask import jsonify
from flask import render_template, request

# from flask import request, jsonify


@app.route("/category", methods=["GET"])
def get_categories():
    select_query = "SELECT * FROM Category"
    categories = db_manager.fetchall(select_query)
    # Close the cursor and connection
    print(categories)
    return render_template("category.html", result=categories)


@app.route("/create/category", methods=["POST", "GET"])
def create_category():
    if request.method == "POST":
        title = request.form["title"]
        insert_query = "INSERT INTO Category (tittle) VALUES ({})".format(
            title)

        # Execute the SQL query with the provided title
        db_manager.query(insert_query)
        return render_template("successfully_created.html")
    else:
        return render_template("create_category.html")


# @app.route("/category/<int:id>", methods = ["GET"])
# def get_single_category(id):
#     try:
#         category = Category.query.get_or_404(id)
#     except:
#         return jsonify({"message": "Object with given id not found"}), 408
#     return jsonify(category.to_dict()), 200

# @app.route("/category/<int:id>", methods = ['DELETE'])
# def delete_category(id):
#     category = Category.query.get_or_404(id)
#     db.session.delete(category)
#     db.session.commit()
#     return jsonify({"message": f"Category with {id} was deleted"}), 202

# @app.route("/category/<int:id>", methods = ['PATCH'])
# def edit_category(id):
#     category = Category.query.get(id)
#     data = request.get_json()
#     if "tittle" in data:
#         category.tittle = data['tittle']
#     db.session.commit()
#     return jsonify({'message': 'Item was successfully edited'}),200
