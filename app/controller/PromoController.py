from flask import request
from app import response, db
from app.model.campaign import Campaign
from app.model.promo import Promo
from datetime import datetime

def index():
    try:
        promo = Promo.query.all()
        data = transform(promo)
        
        return response.ok(data, "")

    except Exception as e:
        print(e)
        return response.badRequest('', e)

def transform(promo):
    data = []
    for i in promo:
        data.append(singleTransform(i))
    return data

def singleTransform(promo):
    data = {
        'id': promo.id,
        'name': promo.name,
        'discount': promo.discount,
        'campaign_id' : promo.campaign_id,
        'max_discount' : promo.max_discount,
        'category_name' : promo.category_name,
        'created_at' : promo.created_at,
        'updated_at' : promo.updated_at

    }
    return data


def show(id):
    try:
        promo = Promo.query.filter_by(id=id).first()

        if not promo:
            return response.badRequest([], 'promo not found')

        data = singleTransform(promo)

        return response.ok(data, "")

    except Exception as e:
        print(e)

def addPromo():
    try:
        name = request.json['name']
        discount = request.json['discount']
        category_name  = request.json['category_name']
        campaign_id = request.json['campaign_id']
        max_discount = request.json['max_discount']
        campaign = Campaign.query.filter_by(id=campaign_id).first()

        # Check if campaign doesnt exist
        if not campaign :
            return response.badRequest('', 'campaign not found')

        promo = Promo.query.filter_by(name=name).first()

        # Check if promo already exist
        if promo :
            return response.badRequest('', 'promo already exist')

        promo = Promo(name=name, 
                    discount=discount,
                    category_name=category_name,
                    campaign_id=campaign_id,
                    max_discount=max_discount
                    )

        db.session.add(promo)
        db.session.commit()

        return response.addData('', 'Promo added')

    except Exception as e:
        print(e)
        return response.badRequest('error', 'Bad request')

def updatePromo(id):
    try:
        name = request.json['name']
        discount = request.json['discount']
        category_name  = request.json['category_name']
        max_discount = request.json['max_discount']
        promo = Promo.query.filter_by(id=id).first()

        # Check if promo not found
        if not promo :
            return response.badRequest('', 'promo not found')

        promo.discount=discount
        promo.name=name
        promo.max_discount = max_discount
        promo.category_name=category_name
        promo.updated_at = datetime.now()
        
        db.session.commit()

        return response.addData('', 'successfully updated')

    except Exception as e:
        print(e)
        return response.badRequest('error', 'Bad request')

def deletePromo(id):
    try:
        promo = Promo.query.filter_by(id=id).first()

        # Check if promo not found
        if not promo :
            return response.badRequest('', 'promo not found')

        db.session.delete(promo)
        db.session.commit()
        return response.ok('', 'promo deleted')

    except Exception as e:
        print(e)
        return response.badRequest('error', 'Bad request')