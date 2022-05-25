from app import db
from datetime import datetime
from app.model.user import User
from app.model.product import Product
<<<<<<< HEAD
=======
from app.model.voucher import Voucher
>>>>>>> f2cbdec057c8f438d1d561182a485db7be1011c7

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Integer, nullable=False)
    transaction_type = db.Column(db.String(140), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    
    product_id = db.Column(db.Integer, db.ForeignKey(Product.id))
    product = db.relationship("Product", backref="transaction")

    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    user = db.relationship("User", backref="transaction")

<<<<<<< HEAD
=======
    voucher_id = db.Column(db.Integer, db.ForeignKey(Voucher.id))
    voucher = db.relationship("Voucher", backref="transaction")

    # campaign_id = db.Column(db.Integer, db.ForeignKey(Campaign.id))
    # campaign = db.relationship("Campaign", backref="transaction")

>>>>>>> f2cbdec057c8f438d1d561182a485db7be1011c7
    def __repr__(self):
        return '<id_transaction: {},user_id: {}>'.format(self.id,self.user_id)

