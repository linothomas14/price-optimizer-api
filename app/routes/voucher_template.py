from flask import jsonify, request
from app import app, response
from app.controller import *
from app.controller.utils import user_voucher
from flask_jwt_extended import *

# Read and add Vouchers
@app.route('/vouchers', methods = ['GET','POST'])
def Voucher():
    if request.method == 'GET':
        return Voucher_tempController.index()
    else :
        return Voucher_tempController.addVoucher()

# CRUD Voucher
@app.route('/vouchers/<int:id>', methods = ['GET','PUT', 'DELETE'])
def Vouchers(id):
    if request.method == 'PUT':
        return Voucher_tempController.updateVoucher(id)
    if request.method == 'DELETE':
        return Voucher_tempController.deleteVoucher(id)
    else :
        return Voucher_tempController.show(id)

# get all user voucher
@app.route('/vouchers/<int:id>/predict', methods=['POST'])
def PredictVoucher(id):
    return user_voucher.predict_users(id)
