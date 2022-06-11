from flask import jsonify, request
from app import app, response
from app.controller.utils import user_voucher
from app.controller import VoucherController

# Read Vouchers
@app.route('/vouchers', methods = ['GET'])
def Voucher():
    page = request.args.get('page', 1)
    return VoucherController.index(page)

@app.route('/vouchers/<int:id>', methods = ['GET'])
def Vouchers(id):
        return VoucherController.show(id)

