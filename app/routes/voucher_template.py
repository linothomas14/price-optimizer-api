from flask import jsonify, request
from app import app, response
from app.controller import Voucher_tempController

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