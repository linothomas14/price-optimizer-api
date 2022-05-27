from flask import jsonify, request
from app import app, response
from app.controller import ProductController
from flask_jwt_extended import *
from app.routes.auth import checkAuth

# Read and add products
@app.route('/products', methods = ['GET','POST'])
def product():
    if request.method == 'GET':
        page = request.args.get('page', 1)
        return ProductController.index(page)
    else :
        isAdmin = checkAuth()
        if isAdmin is False:
            return response.badRequest('','auth not recognized')
        return ProductController.addProduct()

# @app.route('/products?=page', methods = ['GET'])
# def getProductPagination(page):
#     isAdmin = checkAuth()
#     if isAdmin is False:
#         return response.badRequest('','auth not recognized')
#     return ProductController.index(page)

# CRUD product
@app.route('/products/<int:id>', methods = ['GET','PUT', 'DELETE'])
def products(id):
    isAdmin = checkAuth()
    if isAdmin is False:
        return response.badRequest('','auth not recognized')
    if request.method == 'PUT':
        return ProductController.updateProduct(id)
    if request.method == 'DELETE':
        return ProductController.deleteProduct(id)
    else :
        return ProductController.show(id)
    
