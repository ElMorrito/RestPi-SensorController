from flask import Flask

from app import models
from app.extensions import db, ma
from app.views import app_blueprint
from api.main import api_blueprint


def create_app():

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///atest.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    ma.init_app(app)
    app.register_blueprint(app_blueprint)
    app.register_blueprint(api_blueprint)
    return app
