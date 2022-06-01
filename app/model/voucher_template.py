from app import db
from datetime import datetime

class TemplateVoucher(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(230), nullable=False)
    discount_percent = db.Column(db.Float, nullable=False)
    budget = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)
    
    def __repr__(self):
        return '<Voucher {}>'.format(self.name)