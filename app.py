from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)

# Set up the SQLAlchemy Database to be a local file 'desserts.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1/capstone_project'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=True)
