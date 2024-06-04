from flask import Flask, render_template, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from validator import validate_product

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/products"
mongo = PyMongo(app)

@app.route('/')
def index():
    products = list(mongo.db.products.find())
    return render_template('index.html', products=products)

@app.route('/add_product', methods=['POST'])
def add_product():
    product = {
        "name": request.form.get('name'),
        "description": request.form.get('description'),
        "price": float(request.form.get('price')),
        "image": request.form.get('image')
    }
    if validate_product(product):
        mongo.db.products.insert_one(product)
        return 'Product added successfully'
    else:
        return 'Invalid product data'

if __name__ == '__main__':
    app.run(debug=True)
