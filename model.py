from app import db


class User(db.Model):
    # See http://flask-sqlalchemy.pocoo.org/2.0/models/#simple-example
    # for details on the column types.
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    # dont forget to set this >> nullable=False
    name = db.Column(db.String(100),)
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))

    def __init__(self, name, email, password, test):
        self.name = name
        self.email = email
        self.password = password
        self.test = test


# def create_user(new_name, new_email, new_password, new_address):
#     # Create a User with the provided input.
#     # At first, we will trust the user.

#     # This line maps to line 16 above (the User.__init__ method)
#     user = User(new_name, new_email, new_password, new_address)

#     # Actually add this user to the database
#     db.session.add(user)

#     # Save all pending changes to the database
#     db.session.commit()

#     return user


if __name__ == "__main__":

    # Run this file directly to create the database tables.
    print("Creating database tables...")
    # db.create_all()
    print("Done!")
