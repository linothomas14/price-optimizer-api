from app import db
from datetime import datetime
# from model.voucher import Voucher

class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(230), nullable=False)
    discount = db.Column(db.Float, nullable=False)
    periodial = db.Column(db.Boolean, default=False, nullable=False)
    start_date = db.Column(db.DateTime, default=datetime.now, nullable=False)
    end_date = db.Column(db.DateTime, default=datetime.now, nullable=False)
    every_weekend = db.Column(db.Boolean, default=False, nullable=False)
    is_active = db.Column(db.Boolean, default=False, nullable=False)
    # voucher = db.relationship('Voucher', backref='campaign', lazy = True)

    def __repr__(self) -> str:
        return '<Campaign {}>'.format(self.name)
    
    
