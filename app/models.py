from app import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(230), nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    transactions = db.relationship('Transaction', backref='author', lazy='dynamic')

    def __init__(self, name, email, password_hash, created_at, updated_at):
        self.name = name
        self.email = email
        self.password_hash = password_hash
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return '<User {}>'.format(self.name)

    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def getAll():
        users = User.query.all()
        result = []
        for user in users:
            obj = {
                'id': user.id,
                'name': user.name,
                'email': user.email,
            }
            result.append(obj)
        return result
    
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

