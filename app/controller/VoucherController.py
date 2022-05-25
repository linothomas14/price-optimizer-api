from flask import request
from app import response, db
from app.model import product
from flask_jwt_extended import *
from app.model.voucher import Voucher
from app.model import product

def index():
    try:
        vouchers = Voucher.query.all()
        data = transform(vouchers)
        return response.ok(data, "")
    except Exception as e:
        print(e)
        return response.badRequest('', e)

def transform(vouchers):
    data = []
    for i in vouchers:
        data.append(singleTransform(i))
    print(data)
    return data

def singleTransform(voucher):
    data = {
        'id': voucher.id,
        'name':voucher.name,
        'discount_percent' : voucher.discount_percent,
        'valid_from' : voucher.valid_from,
        'valid_to' : voucher.valid_to,
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

def addVoucher():
    try:
        name = request.json['name']
        discount_percent = request.json['discount']
        voucher = Voucher.query.filter_by(name=name).first()

        voucher = Voucher(name=name, discount_percent=discount_percent)
        db.session.add(voucher)
        db.session.commit()
        return response.addData('', 'Voucher added succesfully.')

    except Exception as e:
        print(e)
        return response.badRequest('error', 'Bad request')

def redeemVoucher(id):
    try:
        voucher_id = id
        voucher = Voucher.query.filter_by(id=voucher_id).first()

        # Check if voucher invalid/fully redeemed
        if not voucher :
            return response.badRequest('', 'Sorry, voucher is fully redeemed or invalid.')

        name = request.json['name']
        discount_percent = request.json['discount']
        totalPrice = discount_percent * product.total_price
        voucher = Voucher(name=name, totalPrice=totalPrice)
        
        db.session.add(voucher)
        db.session.commit()
        return response.ok('Voucher Applied.')

    except Exception as e:
        print(e)
        return response.badRequest('error', 'Bad request')


def cancelVoucher(id):
    try:
        voucher = Voucher.query.filter_by(id=id).first()

        # Check if product not found
        if not voucher :
            return response.badRequest('', 'There is no voucher applied.')

        db.session.delete(voucher)
        db.session.commit()
        return response.ok('', 'Voucher canceled.')

    except Exception as e:
        print(e)
        return response.badRequest('error', 'Bad request')




