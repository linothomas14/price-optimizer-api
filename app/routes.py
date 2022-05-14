from crypt import methods
from flask import jsonify,request
from app import app,db,response
from app.model.user import User
from app.controller import UserController


@app.route('/')
@app.route('/index')
def index():
    return jsonify({"msg" : "This is price-optimizer-api"})

# Read all users
@app.route('/users', methods = ['GET'])
def user():
    return UserController.index()

# Read userById
@app.route('/users/<int:id>', methods = ['GET'])
def user_get(id):
    user_id = id
    u = User.query.get(user_id)
    data = {
            'user': {
                'id': u.id,
                'name': u.name,
            }
        }

    return response.ok(data,"")


# User Register
@app.route('/users/register', methods = ['POST'])
def user_register():
    

    return response.ok("haha","")

# User Login
@app.route('/users/login', methods = ['POST'])
def user_login():

    

    return response.ok("haha","")