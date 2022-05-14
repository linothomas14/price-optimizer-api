from flask import jsonify
from app.model.user import User
from app import response, app


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

def singleTransform(users):
    data = {
        'id': users.id,
        'name': users.name,
        'email': users.email
    }
    return data

def show(id):
    try:
        users = User.query.filter_by(id=id).first()
        if not users:
            return response.badRequest([], 'Empty....')

        data = singleTransform(users)
        return response.ok(data, "")
    except Exception as e:
        print(e)