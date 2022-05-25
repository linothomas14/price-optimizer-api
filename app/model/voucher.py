from app import db
from datetime import datetime
# from app.model.campaign import Campaign

class Voucher(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(250), nullable=False)
    discount_percent = db.Column(db.Float, nullable=False)
    totalPrice = db.Column(db.Integer, primary_key=True, autoincrement=True)
    valid_from = db.Column(db.DateTime, default=datetime.now)
    valid_to = db.Column(db.DateTime, default=datetime.now)

    # campaign_id = db.Column(db.Integer, db.ForeignKey(Campaign.id))
    # campaign = db.relationship("Campaign", backref="Voucher")

    isActive = db.Column(db.Boolean)

    def __str__(self):
        return self.code


        
    

