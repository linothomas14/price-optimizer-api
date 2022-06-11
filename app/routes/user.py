from flask import jsonify, request
from app import app
from app.controller import UserController, ProductController

@app.route('/')
def index():
    return jsonify({"msg" : "This is price-optimizer-api"})

# @app.route('/reset-db')
# def index():
#     return ProductController.resetDB()

# Read all users
@app.route('/users', methods = ['GET'])
def user():
    page = request.args.get('page',1)
    return UserController.index(page)

# Read userById
@app.route('/users/<string:id>', methods = ['GET'])
def user_get(id):
    return UserController.show(id)
