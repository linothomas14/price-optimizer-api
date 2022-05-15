from crypt import methods
from flask import jsonify,request
from app import app,db,response
from app.model.user import User
from app.controller import UserController
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
