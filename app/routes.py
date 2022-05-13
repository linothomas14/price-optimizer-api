from crypt import methods
from flask import jsonify,request
from app import app,db
from app.models import User


@app.route('/')
@app.route('/index')
def index():
    return jsonify({"msg" : "This is price-optimizer-api"})

@app.route('/user', methods = ['GET','POST'])
def user():
    if request.method == 'GET':
        users= User.query.all()
        result = []
        for user in users:
            obj = {
                'name' : user.name,
                'email' : user.email,
                'method' : request.method
            }   
            result.append(obj)
        return jsonify(result)

    elif request.method == 'POST':
        
        """
        Ngambil data dari JSON parse ke db.session.add(u) -> db.session.commit()
        baru return success
        """
        return jsonify({"msg": "Success"})


@app.route('/user/<int:id>', methods = ['GET'])
def user_get(id):
    user_id = id
    u = User.query.get(user_id)
    construct = {
            'user': {
                'id': u.id,
                'name': u.name,
            }
        }

    return jsonify(construct)
