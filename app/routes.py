from flask import jsonify, request
from app import app, response
from app.controller import TransactionController, UserController, ProductController
from flask_jwt_extended import *

@app.route('/')
def index():
    return jsonify({"msg" : "This is price-optimizer-api"})

# Read all users
@app.route('/users', methods = ['GET'])
def user():
    return UserController.index()

# Read userById
@app.route('/users/<int:id>', methods = ['GET'])
def user_get(id):
    return UserController.show(id)

# User Register
@app.route('/users/register', methods = ['POST'])
def user_register():
    return UserController.register()

# User Login
@app.route('/users/login', methods = ['POST'])
def user_login():
    return UserController.login()

# Read and add products
@app.route('/products', methods = ['GET','POST'])
def product():
    if request.method == 'GET':
        return ProductController.index()
    else :
        isAdmin = checkAuth()
        if isAdmin is False:
            return response.badRequest('','auth not recognized')
        return ProductController.addProduct()

# Update product
@app.route('/products/<int:id>', methods = ['PUT'])
def product_update(id):
    isAdmin = checkAuth()
    if isAdmin is False:
        return response.badRequest('','auth not recognized')
    
    return ProductController.updateProduct(id)
    
# Delete product
@app.route('/products/<int:id>', methods = ['DELETE'])
def product_delete(id):
    isAdmin = checkAuth()
    if isAdmin is False:
        return response.badRequest('','auth not recognized')

    return ProductController.deleteProduct(id)

# Buy Product
@app.route('/buy/<int:product_id>', methods = ['POST'])
@jwt_required()
def product_buy(product_id):
    user_identity = get_jwt_identity()
    user_id = user_identity['id']
    return TransactionController.store(user_id, product_id)

# Get transacition
@app.route('/transactions/', methods = ['GET'])
# @jwt_required()
def get_transaction():
    return TransactionController.index()


# Return True if user role is admin
@jwt_required()
def checkAuth():
    user_identity = get_jwt_identity()
    return True if user_identity['role'] == 'admin' else False
    
    