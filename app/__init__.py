
import click
from flask import Flask
from flask.cli import with_appcontext

from app.database import models
from app.admin import admin
from app.database import db
from app.extensions import ma, security
from app.views import app_blueprint
from app.api import api_blueprint


from flask_security import SQLAlchemyUserDatastore

user_datastore = SQLAlchemyUserDatastore(db, models.Users, models.Roles)


@click.command(name='create-db')
@with_appcontext
def create_db():
    db.create_all()


@click.command(name='create-user')
@click.argument('mail')
@click.argument('password')
@with_appcontext
def create_user(mail, password):
    user_datastore.create_user(email=mail, password=password)
    db.session.commit()


def create_app():

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///atest.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = "Thisissecret"
    # app.config['FLASK_ADMIN_SWATCH'] = 'Cerulean'

    db.init_app(app)
    ma.init_app(app)

    admin.init_app(app)

    app.register_blueprint(app_blueprint)
    app.register_blueprint(api_blueprint)

    security.init_app(app)

    app.cli.add_command(create_db)
    app.cli.add_command(create_user)

    return app
