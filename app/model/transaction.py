from app import db
from datetime import datetime
from app.model.user import User

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(140))
    price = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime,index=True, default=datetime.utcnow)
    transaction_type = db.Column(db.String(140))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, product, price, timestamp, user_id, transaction_type):
        self.product = product
        self.price = price
        self.timestamp = timestamp
        self.transaction_type = transaction_type
        self.user_id = user_id
        

    def __repr__(self):
        return '<id_transaction: {},user_id: {}>'.format(self.id,self.user_id)

    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def getAll():
        pass
    
    def getById():
        """
            Get user by id
        """
        pass 

    def update():
        """
            Update user by id
        """
        pass

    def delete(self):
        db.session.delete(self)
        db.session.commit()

