import os
from flask import request
from app.model.user import User
from app import response, app, db
from flask_jwt_extended import *


def index():
    try:
        users = User.query.all()
        data = transform(users)
        return response.ok(data, "")
    except Exception as e:
        print(e)
        return response.badRequest([], message=e)


def transform(users):
    data = []
    for i in users:
        data.append(singleTransform(i))
    return data

def singleTransform(user):
    data = {
        'id': user.id,
        'name': user.name,
        'email': user.email,
        'role' : user.role
    }
    return data

def show(id):
    try:
        user = User.query.filter_by(id=id).first()
        if not user:
            return response.badRequest([], 'user not found')

        data = singleTransform(user)
        return response.ok(data, "")
    except Exception as e:
        print(e)

def register():
    try:
        name = request.json['name']
        email = request.json['email']
        password = request.json['password']
        user = User.query.filter_by(email=email).first()

        # Check if user already exist
        if user :
            return response.badRequest('', 'user already exist')

        user = User(name=name, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return response.addData('', 'register success')
        

    except Exception as e:
        print(e)
        return response.badRequest('error', 'Bad request')

def login():
    try:
        email = request.json['email']
        password = request.json['password']

        user = User.query.filter_by(email=email).first()
        if not user:
            return response.badRequest([], 'User not found')

        if not user.check_password(password):
            return response.badRequest([], 'Your credentials is invalid')

        data = {
            'id' : user.id,
            'email' : user.email,
            'role' : user.role}
        access_token = create_access_token(data)

        return response.ok(
            {
            "token": access_token,
            }, "")

    except Exception as e:
        print(e)
        return response.badRequest('error', 'Bad request')

@app.cli.command('db_seed')
def db_seed():
    user = User(name="admin", email="admin@gmail.com")
    user.set_password(str(os.environ.get("PASSWORD_ADMIN")))
    user.role = 'admin'
    print("Adding user: %s" % user)
    db.session.add(user)
    db.session.commit()

