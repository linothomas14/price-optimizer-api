from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(230), nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
<<<<<<< HEAD
    role = db.Column(db.String(50), nullable=False, default='user')
=======
    role= db.Column(db.String(50), nullable=False, default='user')
>>>>>>> f2cbdec057c8f438d1d561182a485db7be1011c7
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)
    # transactions = db.relationship('Transaction', lazy='select',backref=db.backref('transactions', lazy='joined'))

    def __repr__(self):
        return '<User {}>'.format(self.name)
<<<<<<< HEAD

    def set_password(self, password): # admin

=======
    
    def getById(self):
        users = User.query.filter_by(email=self.email).first()
        if not users :
            return 1

    def set_password(self, password):
>>>>>>> f2cbdec057c8f438d1d561182a485db7be1011c7
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
<<<<<<< HEAD
=======

        
    

>>>>>>> f2cbdec057c8f438d1d561182a485db7be1011c7
