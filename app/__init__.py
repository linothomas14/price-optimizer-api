from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.model import user, product, transaction, campaign, promo, voucher, voucher_template
from app.routes import user, product, transaction, campaign, promo, voucher, voucher_template