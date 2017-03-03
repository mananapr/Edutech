from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

page = Flask(__name__, static_url_path='/static')
page.config.from_object('config')

db = SQLAlchemy(page)
migrate = Migrate(page, db)

from app import views, models
