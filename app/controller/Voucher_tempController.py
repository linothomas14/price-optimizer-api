from flask import request
from app import response, db
from app.model.voucher_template import TemplateVoucher
from flask_jwt_extended import *
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
        'discount_percent': templateVoucher.discount_percent,
        'budget': templateVoucher.budget,
        'created_at': templateVoucher.created_at,
        'update_at': templateVoucher.update_at

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
        discount_percent = request.json['discount_percent']
        budget = request.json['budget']
        
        templateVoucher = TemplateVoucher.query.filter_by(name=name).first()

        # Check if campaign already exist
        if templateVoucher :
            return response.badRequest('', 'campaign already exist')

        templateVoucher = TemplateVoucher(name=name, 
                            discount_percent=discount_percent,
                            budget=budget, 
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
        discount_percent = request.json['discount_percent']
        budget = request.json['budget']
        
        templateVoucher = TemplateVoucher.query.filter_by(id=id).first()


        # Check if campaign not found
        if not templateVoucher :
            return response.badRequest('', 'Voucher not found')

        templateVoucher.name=name
        templateVoucher.discount_percent=discount_percent
        templateVoucher.budget=budget
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

