from flask import request
from app.model.product import Product
from app import response, app, db
import datetime
from flask_jwt_extended import *
from datetime import datetime

def index():
    try:
        products = Product.query.all()
        data = transform(products)
        return response.ok(data, "")
    except Exception as e:
        print(e)
        return response.badRequest([], message=e)


def transform(products):
    data = []
    for i in products:
        data.append(singleTransform(i))
    return data

def singleTransform(product):
    data = {
        'id': product.id,
        'name': product.name,
        'base_price': product.base_price,
        'competitor_price' : product.competitor_price,
        'created_at' : product.created_at
    }
    return data

def show(id):
    try:
        product = Product.query.filter_by(id=id).first()
        if not product:
            return response.badRequest([], 'product not found')

        data = singleTransform(product)
        return response.ok(data, "")
    except Exception as e:
        print(e)


def addProduct():
    try:
        name = request.json['name']
        base_price = request.json['base_price']
        product = Product.query.filter_by(name=name).first()

        # Check if product already exits
        if product :
            return response.badRequest('', 'product already exits')

        product = Product(name=name, base_price=base_price, competitor_price=base_price)
        # nanti scrap 
        # product.set_competitor_price(set_competitor_price)
        db.session.add(product)
        db.session.commit()
        return response.addData('', 'Product added')

    except Exception as e:
        print(e)
        return response.badRequest('error', 'Bad request')

def updateProduct(id):
    try:
        base_price = request.json['base_price']
        product = Product.query.filter_by(id=id).first()

        # Check if product not found
        if not product :
            return response.badRequest('', 'product not found')

        product.base_price=base_price
        product.competitor_price = base_price
        product.updated_at = datetime.now()
        # nanti scrap 
        # product.set_competitor_price(set_competitor_price)
        # db.session.update(product)
        db.session.commit()
        return response.addData('', 'update success')

    except Exception as e:
        print(e)
        return response.badRequest('error', 'Bad request')

def deleteProduct(id):
    try:
        product = Product.query.filter_by(id=id).first()

        # Check if product not found
        if not product :
            return response.badRequest('', 'product not found')

        db.session.delete(product)
        db.session.commit()
        # nanti scrap 
        # product.set_competitor_price(set_competitor_price)
        return response.ok('', 'delete product success')

    except Exception as e:
        print(e)
        return response.badRequest('error', 'Bad request')



