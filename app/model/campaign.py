from app import db
from datetime import datetime

class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(230), nullable=False)
    periodical = db.Column(db.Boolean, default=False, nullable=False)
    start_date = db.Column(db.DateTime, default=datetime.now, nullable=False)
    end_date = db.Column(db.DateTime, default=datetime.now, nullable=False)
    every_weekend = db.Column(db.Boolean, default=False, nullable=False)
    is_active = db.Column(db.Boolean, default=False, nullable=False)
    promo = db.relationship('Promo', backref='campaign', lazy = True)

    def __repr__(self) -> str:
        return '<Campaign {}>'.format(self.name)
    
    
