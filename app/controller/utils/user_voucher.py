import tensorflow as tf
import pandas as pd

def read_transactions():
    try:
        return pd.read_csv("./final-data/transactions_user.csv")
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

def get_customer_id(customer_idx):
    try:
#         list_customer_orders = list_customer_orders_()
        return list_customer_orders[list_customer_orders.customer_index == customer_idx].customer_unique_id.values[0]
    except Exception as e :
        print(e)
        return response.badRequest('', e)

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

def generate_voucher_for_user(customers, product_category, transactionss, list_product_in_uses, list_customer_orderss):
    try:
        transactions = transactionss
        list_product_in_use = list_product_in_uses
        list_customer_orders = list_customer_orderss

        
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
        budget = 100000000
        product_category = 'sports_leisure'
        budget_per_user  = 60000
        
        transactions = read_transactions()
        list_product_in_use = list_product_in_use_(transactions)
        list_customer_orders = list_customer_orders_(transactions)
        
        # preparation
        model = tf.keras.models.load_model("./model/voucher_model_3.h5")
        list_customers_will_get_voucher =  get_list_loyal_customers_(transactions)[0:round(budget/budget_per_user)]
        
        # predict users
        result = []
        for customers in list_customers_will_get_voucher:
            list_voucher = generate_voucher_for_user(customers, product_category, transactions, list_product_in_use, list_customer_orders)
            mydict ={}
            mydict["id"] = customers
            mydict['voucher'] = list_voucher
            result.append(mydict)

        return result
        
    except Exception as e :
        print(e)
        return response.badRequest('',e)