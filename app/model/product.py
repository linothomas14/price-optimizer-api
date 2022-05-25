from app import db
from datetime import datetime

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(230), nullable=False)
    base_price = db.Column(db.Integer, nullable=False)
    competitor_price = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)
    

    def __repr__(self):
        return '<Product {}>'.format(self.name)
    

<<<<<<< HEAD
        
=======
>>>>>>> cdbf2f95462842c439484a2a55b316ecca3e0fd3
    

