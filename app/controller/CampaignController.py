from flask import request
from app import response, db
from app.model.campaign import Campaign
from app.controller import PromoController
from app.model.product import Product
from app.model.promo import Promo

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
        'periodical' : campaign.periodical,
        'start_date' : campaign.start_date,
        'end_date' : campaign.end_date,
        'every_weekend' : campaign.every_weekend,
        'is_active' : campaign.is_active,
        'promo' : PromoController.transform(campaign.promo),
        'created_at' : campaign.created_at,
        'updated_at' : campaign.updated_at

    }
    return data

def show(id):
    try:
        campaign = Campaign.query.filter_by(id=id).first()

        if not campaign:
            return response.badRequest([], 'campaign not found')

        data = singleTransform(campaign)

        return response.ok(data, "")

    except Exception as e:
        print(e)

def addCampaign():
    try:
        name = request.json['name']
        periodical = request.json['periodical']
        start_date = request.json['start_date']
        end_date = request.json['end_date']
        every_weekend = request.json['every_weekend']

        campaign = Campaign.query.filter_by(name=name).first()

        # Check if campaign already exist
        if campaign :
            return response.badRequest('', 'campaign already exist')

        campaign = Campaign(name=name, 
                            periodical=periodical, 
                            start_date=start_date, 
                            end_date=end_date,
                            every_weekend=every_weekend,
                            )

        db.session.add(campaign)
        db.session.commit()

        return response.addData('', 'Campaign added')

    except Exception as e:
        print(e)
        return response.badRequest('error', 'Bad request')

def updateCampaign(id):
    try:
        name = request.json['name']
        periodical = request.json['periodical']
        start_date = request.json['start_date']
        end_date = request.json['end_date']
        every_weekend = request.json['every_weekend']
        is_active = request.json['is_active']

        campaign = Campaign.query.filter_by(id=id).first()

        # Check if campaign not found
        if not campaign :
            return response.badRequest('', 'campaign not found')

        campaign.name=name
        campaign.periodical=periodical
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
def predictDemand(id_campaign):
    try:
        #Ambil discount, startDate dan endDate, category product disetiap promo
        #Ambil history transaksi
        #jalanin ML
        #output JSON
    except Exception as e:
        print(e)
'''

def applyCampaign():
    try:
        promos = []

        # Search campaign
        campaigns = Campaign.query.filter_by(is_active=True).all()
        for campaign in campaigns:
            # get promos in campaign
            for promo in campaign.promo:
                products = Product.query.filter_by(product_category = promo.category_name).all()
                promos.append(promo)
                # check if category name is in products
                if not products :
                    continue

                # edit one by one product in products(by_category)
                for product in products :
                    product.discount += promo.discount
                    
                    # check if discount final price is higher than max discount per promo
                    if product.base_price * product.discount > promo.max_discount:
                        product.final_price = product.base_price - promo.max_discount 
                    else :
                        product.final_price = product.base_price - (product.base_price * product.discount)

        db.session.commit()
        print(promos)
        return response.ok('', 'OK')
    except Exception as e:
        print(e)
        return response.badRequest('error', 'Bad request')
