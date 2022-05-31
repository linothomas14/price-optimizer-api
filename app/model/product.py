from app import db
from datetime import datetime

class Product(db.Model):
    id = db.Column(db.String(200), primary_key=True)
    product_category = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(230), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)
    base_price = db.Column(db.Float, nullable=False)
    competitor_price = db.Column(db.Integer, default=0)
    
    

    def __repr__(self):
        return '<Product {}>'.format(self.name)
    

        
    

