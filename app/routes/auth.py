from flask_jwt_extended import *

@jwt_required()
def checkAuth():
    user_identity = get_jwt_identity()
    return True if user_identity['role'] == 'admin' else False
