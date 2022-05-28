from app import db

from app.model.campaign import Campaign

class Promo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(230), nullable=False)
    discount = db.Column(db.Float, nullable=False)
    campaign_id = db.Column(db.Integer ,db.ForeignKey(Campaign.id))
    category_name = db.Column(db.String(200), nullable=False)
    # campaign = db.relationship('Voucher', backref='campaign', lazy = True)

    def __repr__(self) -> str:
        return '<Promo {}>'.format(self.name)
    
    
