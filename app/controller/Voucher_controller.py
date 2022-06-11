import os
from flask import request
from app.model.voucher import Voucher
from app import response, app, db


def index(page):
    try:
        offset = (int(page) - 1) * 10
        vouchers = Voucher.query.offset(offset).limit(10).all()
        data = transform_voucher(vouchers)
        return response.ok(data, "")
    except Exception as e:
        print(e)
        return response.badRequest([], message=e)

def transform_voucher(vouchers):
    data = []
    for i in vouchers:
        data.append(singleTransform(i))
    return data

def singleTransform(voucher):
    data = {
        'id': voucher.id,
        'max_discount' : voucher.max_discount,
        'product_id' : voucher.product_id,
        'name': voucher.name,
    }
    return data

def show(id):
    try:
        voucher = Voucher.query.filter_by(id=id).first()
        if not voucher:
            return response.badRequest([], 'voucher not found')

        data = singleTransform(voucher)
        return response.ok(data, "")
    except Exception as e:
        print(e)

'''
def assignVoucher(id_voucher):
    try:
        
    except Exception as e:
        print(e)
'''