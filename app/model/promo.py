from app import db
from datetime import datetime
from app.model.campaign import Campaign

class Promo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(230), nullable=False)
    discount = db.Column(db.Float, nullable=False)
    campaign_id = db.Column(db.Integer ,db.ForeignKey(Campaign.id))
    category_name = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)
    
    def __repr__(self) -> str:
        return '<Promo {}>'.format(self.name)
    
    
