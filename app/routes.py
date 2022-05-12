from crypt import methods
from flask import jsonify
from app import app


@app.route('/')
@app.route('/index')
def index():
    return jsonify({"msg" : "This is price-optimizer-api"})

@app.route('/users', methods = ['GET'])
def user_list():
    return jsonify({"msg" : "Test user"})

@app.route('/users/<int:city_id>', methods = ['GET'])
def user_list():
    return jsonify({"msg" : "Test user"})

@app.route('/users', methods = ['POST'])
def register_user():
    return jsonify({"msg": "Success"})