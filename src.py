from flask import Flask, request, json, jsonify, Response
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
import urllib

app = Flask(__name__)
prefix = 'mongodb+srv://admin:'
user = urllib.parse.quote('admin@123')
suffix = '@db01.yj3hr.mongodb.net/shopping'
app.config['MONGO_URI'] = prefix + user + suffix

#mongodb+srv://admin:admin@123@db01.yj3hr.mongodb.net/test

mongo = PyMongo(app)

@app.route('/add', methods = ['POST'])
def add_product():
    _json = request.json
    prod_name = _json['name']
    prod_quantity = _json['quantity']

    if prod_name and prod_quantity and request.method == "POST":
        id = mongo.db.shopping.insert({'name':prod_name, 'quantity':prod_quantity})
        resp = jsonify("Product added succesfully")
        resp.status_code = 200
        return resp
    else:
        return not_found()

@app.route('/products')
def products():
    prods = mongo.db.shopping.find()
    resp = dumps(prods)
    return resp

@app.route('/product/<name>')
def prod(name):
    prod = mongo.db.shopping.find_one({"name":name})
    resp = dumps(prod)
    return resp

@app.route('/delete/<name>', methods = ['DELETE'])
def delete_product(name):
    mongo.db.shopping.delete_one({'name': name})
    resp = jsonify("Product deleted successfully")
    resp.status_code = 200
    return resp

@app.route('/update/<id>', methods = ['PUT'])
def update_product(id):
    _id = id
    _json = request.json
    prod_name = _json['name']
    prod_quantity = _json['quantity']

    if prod_name and _id and prod_quantity and request.method == "PUT":
        mongo.db.shopping.update_one({'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, {'$set': {'name': prod_name, 'quantity': prod_quantity}})
        
        resp = jsonify("Product updated succesfully")
        resp.status_code = 200
        return resp
    else:
        return not_found()

@app.errorhandler(404)
def not_found(error = None):
    message = {
        'status' : 400,
        'message': 'Not Found' + request.url
    }
    resp = jsonify(message)
    resp.status_code =404
    return resp


if __name__ == "__main__":
    app.run(debug = True)