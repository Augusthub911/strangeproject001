from bson import ObjectId
from flask_pymongo import PyMongo

class ProductModel:
    def __init__(self, mongo):
        self.mongo = mongo
        self.collection = mongo.db.products

    def get_all_products(self):
        return list(self.collection.find())

    def get_product(self, product_id):
        return self.collection.find_one({'_id': ObjectId(product_id)})

    def add_product(self, product):
        return self.collection.insert_one(product)

    def update_product(self, product_id, product):
        return self.collection.update_one({'_id': ObjectId(product_id)}, {'$set': product})

    def delete_product(self, product_id):
        return self.collection.delete_one({'_id': ObjectId(product_id)})
