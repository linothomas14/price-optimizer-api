from flask import request
from app import response, db
from app.model.campaign import Campaign
from flask_jwt_extended import *

def index():
    try:
        campaign = Campaign.query.all()
        data = transform(campaign)
        return response.ok(data, "")
    except Exception as e:
        print(e)
        return response.badRequest('', e)

def transform(campaign):
    data = []
    for i in campaign:
        data.append(singleTransform(i))
    return data

def singleTransform(campaign):
    data = {
        'id': campaign.id,
        'name': campaign.name,
        'discount': campaign.discount,
        'periodial' : campaign.periodial,
        'start_date' : campaign.start_date,
        'end_date' : campaign.end_date,
        'every_weekend' : campaign.every_weekend,
        'is_active' : campaign.is_active
    }
    return data

def addCampaign():
    try:
        name = request.json['name']
        discount = request.json['discount']
        campaign = Campaign.query.filter_by(name=name).first()

        # Check if campaign already exits
        if campaign :
            return response.badRequest('', 'campaign already exits')

        campaign = Campaign(name=name, discount=discount)
        db.session.add(campaign)
        db.session.commit()
        return response.addData('', 'Campaign added')

    except Exception as e:
        print(e)
        return response.badRequest('error', 'Bad request')

def updateCampaign(id):
    try:
        name = request.json['name']
        discount = request.json['discount']
        periodial = request.json['periodial']
        start_date = request.json['start_date']
        end_date = request.json['end_date']
        every_weekend = request.json['every_weekend']
        is_active = request.json['is_active']
        campaign = Campaign.query.filter_by(id=id).first()

        # Check if campaign not found
        if not campaign :
            return response.badRequest('', 'campaign not found')

        campaign.name=name
        campaign.discount=discount
        campaign.periodial=periodial
        campaign.start_date=start_date
        campaign.end_date=end_date
        campaign.every_weekend=every_weekend
        campaign.is_active=is_active
        db.session.commit()
        return response.addData('', 'successfully updated')

    except Exception as e:
        print(e)
        return response.badRequest('error', 'Bad request')

def deleteCampaign(id):
    try:
        campaign = Campaign.query.filter_by(id=id).first()

        # Check if campaign not found
        if not campaign :
            return response.badRequest('', 'campaign not found')
        db.session.delete(campaign)
        db.session.commit()
        return response.ok('', 'campaign deleted')

    except Exception as e:
        print(e)
        return response.badRequest('error', 'Bad request')

'''
def changeActive(id):
    try:
        is_active = request.json['is_active']
        campaign =Campaign.query.filter_by(id=id).first()
        # Check if campaign not found
        if not campaign :
            return response.badRequest('', 'campaign not found')

        campaign.is_active=is_active
        db.session.commit()
        if is_active is True:
            return response.addData('', 'Campaign Turned ON')
        else :
            return response.addData('', 'Campaign Turned OFF')
    except Exception as e:
        print(e)
        return response.badRequest('error', 'Bad request')
'''




