from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_whooshee import Whooshee
from authomatic import Authomatic
from authomatic.providers import oauth2

page = Flask(__name__, static_url_path='/static')
page.config.from_object('config')

UPLOAD_FOLDER = '/home/manan/Programs/EduTech/app/static/userdata/'
page.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

CONFIG = {
    'google': {
        'class_': oauth2.Google,
        'consumer_key': '1005905952791-tfb0dpv4iomdr0edhtdpnl9mnu0t0nsp.apps.googleusercontent.com',
        'consumer_secret': 'u5qpMJhO8P-g4HF2wB7z4nwb',
        'scope': oauth2.Google.user_info_scope
    }
}

authomatic = Authomatic(CONFIG, 'random secret string for session signing')

db = SQLAlchemy(page)
migrate = Migrate(page, db)

whooshee = Whooshee(page)

from app import views, models
