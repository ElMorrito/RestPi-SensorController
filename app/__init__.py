from flask import Flask

from app import models
from app.extensions import db, ma, admin, security
from app.views import app_blueprint
from api.main import api_blueprint

from flask_admin.contrib.sqla import ModelView
from flask_security import SQLAlchemyUserDatastore

user_datastore = SQLAlchemyUserDatastore(db, models.Users, models.Roles)


class UserModelView(ModelView):
    column_exclude_list = ['password', ]


def create_app():

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///atest.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = "Thisissecret"
    #app.config['FLASK_ADMIN_SWATCH'] = 'Cerulean'

    db.init_app(app)
    ma.init_app(app)

    admin.init_app(app)
    admin.add_view(ModelView(models.Sensor, db.session))
    admin.add_view(UserModelView(models.Users, db.session))
    admin.add_view(ModelView(models.Roles, db.session))

    app.register_blueprint(app_blueprint)
    app.register_blueprint(api_blueprint)

    security.init_app(app)

    return app
