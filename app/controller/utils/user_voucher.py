import tensorflow as tf
import pandas as pd

import warnings
warnings.filterwarnings('ignore')

from flask import request
from app import response, db
from app.model.campaign import Campaign
from app.controller import PromoController
from app.model.product import Product
from app.model.promo import Promo
from app.model.transaction import Transaction
from app.controller.utils import demand_estimator 


def get_transaction_all():
    try:
        transaction = Transaction.index()
    except Exception as e :
        print(e)
        return response.badRequest('', e)
