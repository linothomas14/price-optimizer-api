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

def PromoSingleTransform(promo):
    data = {
        'total_discount': promo.discount,
        'total_max_discount' : promo.max_discount,
        'category_name' : promo.category_name,

    }
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
        campaigns =Campaign.query.filter_by(id=id).first()

        # Check if campaign not found
        if not campaigns :
            return response.badRequest('', 'campaign not found')

        if campaigns.is_active == is_active :
            return response.badRequest('', 'already same status')
        campaigns.is_active=is_active
        
        
        # print(campaign['discount'])
        if is_active is True:

            campaign = getPromoCampaignById(id)

            for cat_name, promo in zip(campaign['category_name'],campaign['discount']):

                products = Product.query.filter_by(product_category = cat_name).all()

                for product in products:
                    
                    product.experiment_discount += promo['total_discount']
                    if product.experiment_discount >= 1:
                        return response.badRequest('', 'Discount reach 100%')

                    product.experiment_price -= getDiffPrice(product.base_price,
                                     promo['total_discount'], 
                                    promo['total_max_discount'])
                                    
            db.session.commit()

            return response.addData('', 'Campaign Turned ON')
        
        else :
            campaign = getPromoCampaignById(id)
            for cat_name, promo in zip(campaign['category_name'],campaign['discount']):
                print('category ',cat_name,'total max discount = ', promo['total_max_discount'])
                products = Product.query.filter_by(product_category = cat_name).all()
                for product in products:
                    product.experiment_discount -= promo['total_discount']
                    
                    # STUCK AT THIS !!!!
                    
                    product.experiment_price += getDiffPrice(product.base_price,
                                    promo['total_discount'], 
                                    promo['total_max_discount'])

            db.session.commit()
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
   
        db.session.query(Product).update({Product.final_price: Product.experiment_price, Product.discount : Product.experiment_discount})
        db.session.commit()
        # print(promos)
        return response.ok('', 'Success')
    except Exception as e:
        print(e)
        return response.badRequest('error', 'Bad request')

def getAllPromoActive():
    category_name = []
    promos = []
    # Search campaign
    campaigns = Campaign.query.filter_by(is_active=True).all()
    for campaign in campaigns:
        # get promos in campaign
        for promo in campaign.promo:
            # get category name of active promo

            if promo.category_name not in category_name :
                category_name.append(promo.category_name)
                promos.append(PromoSingleTransform(promo))
            else :
                for a in promos :

                    if promo.category_name == a['category_name'] :
                        a['total_max_discount'] += promo.max_discount
                        a['total_discount'] += promo.discount
    result = {
        'category_name' : category_name,
        'discount' : promos
    }
    return result

def getPromoCampaignById(id):

    category_name = []
    promos = []
    # Search campaign
    campaign = Campaign.query.filter_by(id=id).first()
    # get promos in campaign
    for promo in campaign.promo:
        # get category name of active promo

        if promo.category_name not in category_name :
            category_name.append(promo.category_name)
            promos.append(PromoSingleTransform(promo))
        else :
            for a in promos :

                if promo.category_name == a['category_name'] :
                    a['total_max_discount'] += promo.max_discount
                    a['total_discount'] += promo.discount
    result = {
        'category_name' : category_name,
        'discount' : promos
    }
    return result

def getFinalProduct():
    data_products = []
    category_products = []
    promos = getAllPromoActive()
    for promo in promos:
        products = Product.query.filter_by(product_category = promo['category_name']).all()

        category_products.append(promo['category_name'])
        # check if category name is in products
        
        if not products :
            continue
    
        # edit one by one product in products(by_category)
        for product in products :
            product.discount = promo['total_discount']
            
            # check if discount final price is higher than max discount per promo
            product.final_price = applyDiscount(product.base_price,
                                                product.discount, 
                                                promo['total_max_discount'])

            data_products.append(product)

    result = {
        'product' : data_products,
        'category' : category_products
    }
    return result

def applyDiscount(base_price,discount,max_discount):
    if base_price * discount > max_discount:
        final_price = base_price - max_discount 
    else :
        final_price = base_price - (base_price * discount)
    return final_price

def getDiffPrice(base_price,discount,max_discount):
    diffPrice = base_price * discount
    return diffPrice if diffPrice < max_discount else max_discount
