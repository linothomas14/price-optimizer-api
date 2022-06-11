from flask import jsonify, request
from app import app, response
from app.controller.utils import user_voucher
from app.controller import Voucher_tempController

# Read and add template Vouchers
@app.route('/template-vouchers', methods = ['GET','POST'])
def TempVoucher():
    if request.method == 'GET':
        return Voucher_tempController.index()
    else :
        return Voucher_tempController.addVoucher()

#   CRUD template Voucher
@app.route('/template-vouchers/<int:id>', methods = ['GET','PUT', 'DELETE'])
def TempVouchers(id):
    if request.method == 'PUT':
        return Voucher_tempController.updateVoucher(id)
    if request.method == 'DELETE':
        return Voucher_tempController.deleteVoucher(id)
    else :
        return Voucher_tempController.show(id)

# get all user voucher
@app.route('/template-vouchers/<int:id>/predict', methods=['POST'])
def PredictVoucher(id):
    return user_voucher.predict_users(id)
