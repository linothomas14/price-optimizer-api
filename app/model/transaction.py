from app import db
from datetime import datetime
from app.model.user import User

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.String(140))
    # amount = db.Column(db.Integer, nullable=False)
    # product = db.relationship("Product", backref="product_id")
    price = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime,index=True, default=datetime.now)
    transaction_type = db.Column(db.String(140))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # users = db.relationship("User", backref="user_id")

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

