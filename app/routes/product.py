from flask import jsonify, request
from app import app, response
from app.controller import ProductController

# Read and add products
@app.route('/products', methods = ['GET','POST'])
def product():
    if request.method == 'GET':
        page = request.args.get('page', 1)
        category = request.args.get('category', "all")
        return ProductController.index(page, category)
    else :
        return ProductController.addProduct()

# CRUD product
@app.route('/products/<string:id>', methods = ['GET','PUT', 'DELETE'])
def products(id):
    if request.method == 'PUT':
        return ProductController.updateProduct(id)
    if request.method == 'DELETE':
        return ProductController.deleteProduct(id)
    else :
        return ProductController.show(id)
    
