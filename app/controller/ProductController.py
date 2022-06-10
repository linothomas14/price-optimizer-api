from flask import request
from app.model.product import Product
from app import response, db
from datetime import datetime
import uuid


def index(page,category,name):
    try:
        offset = (int(page) - 1) * 10
        if name != "all" :
            search = "%{}%".format(name)
            products = Product.query.filter(Product.name.like(search)).offset(offset).limit(10).all()
        elif category !="all":
            products = Product.query.filter_by(product_category=category).offset(offset).limit(10).all()
        else :
            products = Product.query.offset(offset).limit(10).all()
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
        'discount': product.discount,
        'final_price' : product.final_price,
        'competitor_price' : product.competitor_price,
        'created_at' : product.created_at,
        'updated_at' : product.updated_at,
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
        product_category = request.json['product_category']
        product = Product.query.filter_by(name=name).first()

        # Check if product already exist
        if product :
            return response.badRequest('', 'product already exist')
        
        id = uuid.uuid4()
        discount_category = Product.query.filter_by(product_category=product_category).first()
        if discount_category :
            final_price= base_price - (base_price * discount_category.discount)
            product = Product(id=id, name=name, 
                              base_price=base_price, 
                              product_category=product_category,
                              discount=discount_category.discount,
                              experiment_discount= discount_category.experiment_discount,
                              competitor_price=base_price,
                              experiment_price=final_price, 
                              final_price=final_price)
        else :
            final_price = base_price
            product = Product(id=id, name=name, base_price=base_price, product_category=product_category,experiment_price=final_price, competitor_price=base_price, final_price=final_price)
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
        name = request.json['name']
        base_price = request.json['base_price']
        product = Product.query.filter_by(id=id).first()

        # Check if product not found
        if not product :
            return response.badRequest('', 'product not found')

        product.name=name
        product.base_price=base_price
        product.final_price= base_price - (base_price * product.discount)
        product.updated_at = datetime.now()
        db.session.commit()
        
        return response.addData('', 'successfully updated')

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
        
        return response.ok('', 'product deleted')

    except Exception as e:
        print(e)
        return response.badRequest('error', 'Bad request')

def resetDB():
    try:
        products = Product.query.all()
        for product in products:
            # product.final_price = product.base_price - (product.base_price * product.discount)
            product.final_price = product.base_price
            product.discount = 0
        db.session.commit()
        return response.ok('', 'OK')
    except Exception as e:
        print(e)
        return response.ok('error', 'Bad Request')
