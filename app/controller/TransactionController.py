from flask import request
from app.controller import ProductController, UserController
from app.model.product import Product
from app.model.transaction import Transaction
from app import response, db
from flask_jwt_extended import *

def index():
    try:
        transactions = Transaction.query.all()
        data = transform(transactions)
        return response.ok(data, "")
    except Exception as e:
        print(e)
        return response.badRequest('', e)


def transform(products):
    data = []
    for i in products:
        data.append(singleTransform(i))
    print(data)
    return data

def singleTransform(transaction):
    data = {
        'id': transaction.id,
        'created_at':transaction.created_at,
        'amount' : transaction.amount,
        'total_price' : transaction.total_price,
        'product_id' : transaction.product_id,
        'product' :ProductController.singleTransform(transaction.product),
        'user_id' : transaction.user_id,
        'user': UserController.singleTransform(transaction.user)
    }
    return data

def show(id):
    try:
        transaction = Transaction.query.filter_by(id=id).first()
        if not transaction:
            return response.badRequest([], 'transaction not found')

        data = singleTransform(transaction)
        return response.ok(data, "")
    except Exception as e:
        print(e)


def store(user_id, product_id):
    try:
        user_id = user_id
        product_id = product_id
        product = Product.query.filter_by(id=product_id).first()
        if not product :
            return response.badRequest('', 'product not found')

        transaction_type = request.json['transaction_type']
        amount = request.json['amount']
        total_price = amount * product.base_price
        transaction = Transaction(user_id=user_id, product_id=product_id, total_price=total_price, transaction_type=transaction_type, amount=amount)
        db.session.add(transaction)
        db.session.commit()
        return response.ok('', 'Successfully create transaction!')

    except Exception as e:
        return response.badRequest('', e)
