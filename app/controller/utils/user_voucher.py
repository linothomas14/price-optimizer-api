import tensorflow as tf
import pandas as pd
from app import app, response, db
from app.controller import *
import numpy as np
from app.model.voucher import Voucher

from app.model.voucher_template import TemplateVoucher

def read_transactions():
    try:
        return pd.read_csv("./assets/data/user_voucher/transactions_user.csv")
    except Exception as e :
        print(e)
        return response.badRequest('', e)

def list_product_in_use_(transactions_):
    try:
        transactions = transactions_
        products = transactions[['product_id','product_category']].drop_duplicates(subset=['product_id'])
        products['product_index'] = np.array([i for i in range(len(products))])
        return products
    except Exception as e :
        print(e)
        return response.badRequest('', e)
    

def list_customer_orders_(transactions_):
    try:
        transactions = transactions_
        customers = transactions[['customer_unique_id']].drop_duplicates(subset=['customer_unique_id'])
        customers['customer_index'] = np.array([i for i in range(len(customers))])
        return customers
    except Exception as e :
        print(e)
        return response.badRequest('', e)

def get_customer_index(customer_id,list_customer_orderss ):
    try:
        list_customer_orders = list_customer_orderss
        return list_customer_orders[list_customer_orders.customer_unique_id == customer_id].customer_index.values[0]
    except Exception as e :
        print(e)
        return response.badRequest('', e)

# def get_customer_id(customer_idx, list_customer_orderss):
#     try:
#         list_customer_orders = list_customer_orderss
#         return list_customer_orders[list_customer_orders.customer_index == customer_idx].customer_unique_id.values[0]
#     except Exception as e :
#         print(e)
#         return response.badRequest('', e)

def get_transaction_by_customer(customer_id, transactions_):
    try:
        transactions = transactions_
        return transactions[transactions.customer_unique_id == customer_id].product_id.values
    except Exception as e :
        print(e)
        return response.badRequest('', e)

def get_product_index_by_product_id(product_id, list_product_in_uses):
    try:
        list_product_in_use = list_product_in_uses
        return list_product_in_use[list_product_in_use.product_id == product_id].product_index.values[0]
    except Exception as e :
        print(e)
        return response.badRequest('', e)

def get_product_category_by_product_index(product_idx, list_product_in_uses):
    try:
        list_product_in_use = list_product_in_uses
        return list_product_in_use[list_product_in_use.product_index == product_idx].product_category.values[0]
    except Exception as e :
        print(e)
        return response.badRequest('', e)

def get_product_id_by_product_index(product_idx, list_product_in_uses):
    try:
        list_product_in_use = list_product_in_uses
        return list_product_in_use[list_product_in_use.product_index == product_idx].product_id.values[0]
    except Exception as e :
        print(e)
        return response.badRequest('', e)

def set_product_index_input(product_not_purchased):
    try:
        return pd.DataFrame(product_not_purchased,columns=['filtered_input']).reset_index()
    except Exception as e :
        print(e)
        return response.badRequest('', e)

def get_list_loyal_customers_(transactions_):
    try:
        transactions = transactions_
        return pd.DataFrame(transactions.customer_unique_id.value_counts()).reset_index().rename({'index':'customer_unique_id', 'customer_unique_id':'count_transaction'}, axis=1).customer_unique_id.values
    except Exception as e :
        print(e)
        return response.badRequest('', e)

def generate_voucher_for_user(models, customers, product_category, transactionss, list_product_in_uses, list_customer_orderss):
    try:
        transactions = transactionss
        list_product_in_use = list_product_in_uses
        list_customer_orders = list_customer_orderss
        model = models
        
        product_customer_purchased = get_transaction_by_customer(customers, transactions)
        index_product_already_purchased = []
        for i in range(len(product_customer_purchased)):
            index_product_already_purchased.append(get_product_index_by_product_id(product_customer_purchased[i], list_product_in_use))
        filtered_product_in_use_category = list_product_in_use[list_product_in_use.product_category == product_category]
        product_not_purchased = np.array(list(set(filtered_product_in_use_category[~filtered_product_in_use_category.product_index.isin(index_product_already_purchased)].product_index.values)))
        input_product_index = set_product_index_input(product_not_purchased)
        index_user = get_customer_index(customers, list_customer_orders)
        user = np.array([index_user for i in range(len(product_not_purchased))])
        
        
        predictions = model.predict([user,product_not_purchased], verbose=0)
        predictions = np.array([a[0] for a in predictions])
        
        voucher_generate = (-predictions).argsort()
        voucher_generate = pd.DataFrame(voucher_generate, columns=['product_index'])
        voucher_generate = voucher_generate.merge(input_product_index, left_on='product_index', right_on='index')['filtered_input'].head(3).values

        user_voucher = [get_product_id_by_product_index(product,list_product_in_use) for product in voucher_generate]
        return user_voucher
    except Exception as e :
        print(e)
        return response.badRequest('', e)

# Main Function 
def predict_users(id):
    try:
        voucher = TemplateVoucher.query.filter_by(id=id).first()
        if not voucher :
            return response.badRequest('',"Template_Voucher id "+ str(id) +" not found")
        budget_per_user  = 3 * voucher.max_discount
        
        transactions = read_transactions()
        list_product_in_use = list_product_in_use_(transactions)
        list_customer_orders = list_customer_orders_(transactions)
        
        # preparation
        model = tf.keras.models.load_model("./assets/model/user_voucher/voucher_model_1.h5")
        list_customers_will_get_voucher =  get_list_loyal_customers_(transactions)[0:round(voucher.budget/budget_per_user)]
        
        # predict users
        result = []
        for customers in list_customers_will_get_voucher:
            list_voucher = generate_voucher_for_user(model,customers, voucher.category_name, transactions, list_product_in_use, list_customer_orders)
            mydict ={}
            mydict["id"] = customers
            mydict['voucher'] = list_voucher
            # voucher = Voucher(name=voucher.name,voucher.)
            result.append(mydict)

        for res in result:
            for r in res['voucher']:
                user = Voucher(name=voucher.name,user_id=res['id'],
                                product_id=r,
                                max_discount=voucher.max_discount)
                db.session.add(user)
        
        db.session.commit()
        return response.ok(result,'ok,'+str(len(result))+' user have voucher')
        # return result
        
    except Exception as e :
        print(e)
        return response.badRequest('',e)