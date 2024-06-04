from flask import Blueprint, request, jsonify
from models.product import ProductModel
from validator import validate_product

product_blueprint = Blueprint('product', __name__)

product_model = ProductModel(mongo)

@product_blueprint.route('/get_all_products', methods=['GET'])
def get_all_products():
    products = product_model.get_all_products()
    return jsonify(products)

@product_blueprint.route('/get_product/<product_id>', methods=['GET'])
def get_product(product_id):
    product = product_model.get_product(product_id)
    if product:
        return jsonify(product)
    else:
        return jsonify({'error': 'Product not found'}), 404

@product_blueprint.route('/add_product', methods=['POST'])
def add_product():
    product = {
        "name": request.json.get('name'),
        "description": request.json.get('description'),
        "price": float(request.json.get('price')),
        "image": request.json.get('image')
    }
    if validate_product(product):
        product_model.add_product(product)
        return jsonify(product)
    else:
        return jsonify({'error': 'Invalid product data'}), 400

@product_blueprint.route('/update_product/<product_id>', methods=['PUT'])
def update_product(product_id):
    product = {
        "name": request.json.get('name'),
        "description": request.json.get('description'),
        "price": float(request.json.get('price')),
        "image": request.json.get('image')
    }
    if validate_product(product):
        product_model.update_product(product_id, product)
        return jsonify(product)
    else:
        return jsonify({'error': 'Invalid product data'}), 400

@product_blueprint.route('/delete_product/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    product_model.delete_product(product_id)
    return jsonify({'message': 'Product deleted successfully'})
