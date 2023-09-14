# from app import db,app
# from flask import request,jsonify
# from models.product import Product 
# from models.category import Category



# @app.route("/product", methods =['POST'])
# def create_product():
#     data = request.get_json()
#     product = Product(
#         name=data['name'],
#         category_id = data['category_id'],
#         count = data['count'],
#         price = data['price'],
#         material = data['material']

#         )
#     db.session.add(product)
#     db.session.commit()
#     return jsonify({'message': 'Item created successfully'}), 201