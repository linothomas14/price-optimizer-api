from flask import request
from app.model.product import Product
from app import response, db
from flask_jwt_extended import *
from datetime import datetime
import uuid


def index(page,category):
    try:
        offset = (int(page) - 1) * 5
        if category == "all":
            print("else")
            products = Product.query.offset(offset).limit(5).all()
        else:
            print("else")
            products = Product.query.filter_by(product_category=category).offset(offset).limit(5).all()
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
        'product_category': product.product_category,
        'competitor_price' : product.competitor_price,
        'created_at' : product.created_at,
        'updated_at' : product.updated_at,
    }
    return data

# def showById(id):

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
        product_category = request.json['product_category']
        product = Product.query.filter_by(name=name).first()

        # Check if product already exist
        if product :
            return response.badRequest('', 'product already exist')
        id = uuid.uuid4()
        discount_category = Product.query.filter_by(product_category=product_category).first().discount
        list_price= base_price - (base_price * discount_category)
        product = Product(id=id, name=name, base_price=base_price, product_category=product_category, competitor_price=base_price, list_price=list_price)
        
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
        product.list_price= base_price - (base_price * product.discount)
        product.updated_at = datetime.now()
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
        
        return response.ok('', 'delete product success')

    except Exception as e:
        print(e)
        return response.badRequest('error', 'Bad request')

def assignFinalPriceProduct():
    try:
        products = Product.query.all()
        for product in products:
            product.final_price = product.base_price - (product.base_price * product.discount)
        db.session.commit()
        return response.ok('', 'OK')
    except Exception as e:
        print(e)
        return response.ok('error', 'Bad Request')