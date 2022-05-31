from app import db
from datetime import datetime
from app.model.user import User
from app.model.product import Product

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_category_name = db.Column(db.String(200), nullable=False)
    order_purchase_time_stamp = db.Column(db.DateTime, default=datetime.now, nullable=False)
    sales = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    
    def __repr__(self):
        return '<id_transaction: {},user_id: {}>'.format(self.id,self.user_id)

