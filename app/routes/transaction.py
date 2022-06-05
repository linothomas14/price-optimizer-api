
from app import app
from app.controller import TransactionController

# # Buy Product
# @app.route('/buy/<int:product_id>', methods = ['POST'])
# @jwt_required()
# def product_buy(product_id):
#     user_identity = get_jwt_identity()
#     user_id = user_identity['id']
#     return TransactionController.store(user_id, product_id)

# # Get transacition
# @app.route('/transactions/', methods = ['GET'])
# # @jwt_required()
# def get_transaction():
#     return TransactionController.index()

