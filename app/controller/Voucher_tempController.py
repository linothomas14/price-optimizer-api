from unicodedata import category
from flask import request
from app import response, db
from app.model.product import Product
from app.model.voucher_template import TemplateVoucher
from datetime import datetime

def index():
    try:
        templateVoucher = TemplateVoucher.query.all()
        data = transform(templateVoucher)
        return response.ok(data, "")
    except Exception as e:
        print(e)
        return response.badRequest([], message=e)

def transform(templateVoucher):
    data = []
    for i in templateVoucher:
        data.append(singleTransform(i))
    return data

def singleTransform(templateVoucher):
    data = {
        'id': templateVoucher.id,
        'name': templateVoucher.name,
        'max_discount': templateVoucher.max_discount,
        'budget': templateVoucher.budget,
        'created_at': templateVoucher.created_at,
        'updated_at': templateVoucher.updated_at,
        'category_name': templateVoucher.category_name,
        'experied_date' : templateVoucher.experied_date

    }
    return data

def show(id):
    try:
        templateVoucher = TemplateVoucher.query.filter_by(id=id).first()
        if not templateVoucher:
            return response.badRequest([], 'template voucher not found')

        data = singleTransform(templateVoucher)
        return response.ok(data, "")
    except Exception as e:
        print(e)

def addVoucher():
    try:
        
        name = request.json['name']
        max_discount = request.json['max_discount']
        budget = request.json['budget']
        category_name = request.json['category_name']
        experied_date = request.json['experied_date']
        
        list_category = Product.query.filter_by(product_category=category_name).all()
        
        if not list_category:
            return response.badRequest('','category name not found')

        templateVoucher = TemplateVoucher(name=name, 
                            max_discount=max_discount,
                            budget=budget, category_name=category_name,
                            experied_date=experied_date
                            )

        db.session.add(templateVoucher)
        db.session.commit()

        return response.addData('', 'Voucher added')

    except Exception as e:
        print(e)
        return response.badRequest('error', 'Bad request')

def updateVoucher(id):
    try:
        name = request.json['name']
        max_discount = request.json['max_discount']
        budget = request.json['budget']
        experied_date = request.json['experied_date']
        category_name = request.json['category_name']
        
        templateVoucher = TemplateVoucher.query.filter_by(id=id).first()


        # Check if campaign not found
        if not templateVoucher :
            return response.badRequest('', 'Voucher not found')

        templateVoucher.name=name
        templateVoucher.max_discount=max_discount
        templateVoucher.budget=budget
        templateVoucher.experied_date=experied_date
        templateVoucher.category_name=category_name
        templateVoucher.update_at=datetime.now()
        db.session.commit()

        return response.addData('', 'successfully updated')

    except Exception as e:
        print(e)
        return response.badRequest('error', 'Bad request')

def deleteVoucher(id):
    try:
        templateVoucher = TemplateVoucher.query.filter_by(id=id).first()

        # Check if campaign not found
        if not templateVoucher :
            return response.badRequest('', 'Voucher not found')

        db.session.delete(templateVoucher)
        db.session.commit()
        return response.ok('', 'Voucher deleted')

    except Exception as e:
        print(e)
        return response.badRequest('error', 'Bad request')

