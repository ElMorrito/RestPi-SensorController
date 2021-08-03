
from flask import Flask, request, jsonify
from flask_security import datastore
from flask_security.datastore import SQLAlchemyUserDatastore
from apps.admin import admin
from database import database
from apps.security import security
from apps.extensions import ma
from apps.app.views import app_blueprint
from apps.api.views import api_bp

from apps.security.models import Users, Roles


user_datastore = SQLAlchemyUserDatastore(
    database.db, Users, Roles)


def create_app():

    app = Flask(__name__)

    app.config.from_object('config.DevelopmentConfig')

    database.init_app(app)

    ma.init_app(app)

    admin.init_app(app)

    app.register_blueprint(app_blueprint)
    app.register_blueprint(api_bp)

    security.init_app(app, datastore=user_datastore)

    # app.cli.add_command(create_db)
    # app.cli.add_command(create_user)

    return app


app = create_app()


# define 404 and 405 error handlers for /api specific routes wich shuold only retrun json


@app.errorhandler(404)
@app.errorhandler(405)
def _handle_api_error(ex):
    if request.path.startswith('/api/'):
        return jsonify(message=str(ex)), ex.code
    else:
        return ex

# @click.command(name='create-db')
# @with_appcontext
# def create_db():
#     database.db.create_all()


# @click.command(name='create-user')
# @click.argument('mail')
# @click.argument('password')
# @with_appcontext
# def create_user(mail, password):
#     user_datastore.create_user(email=mail, password=password)
#     database.db.session.commit()


if __name__ == "__main__":
    app.run(debug=True)
