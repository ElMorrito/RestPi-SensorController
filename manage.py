
from flask import Flask, request, jsonify
from database import database
from models import User
from apps.admin import admin
from apps.auth import auth
from apps.api import api
from apps.api.views import api_bp


def create_app():

    app = Flask(__name__)

    app.config.from_object('config.DevelopmentConfig')

    database.init_app(app)

    api.init_app(app)

    admin.init_app(app)

    auth.init_app(app)

    app.register_blueprint(api_bp)
    # app.register_blueprint(auth_bp)
    # app.cli.add_command(create_db)
    # app.cli.add_command(create_user)

    return app


app = create_app()


@app.before_first_request
def create_admin():

    if User.query.filter_by(email='admin').first() is None:
        admin = User(email="admin", password="admin")
        database.db.session.add(admin)
        database.db.session.commit()

# define 404 and 405 error handlers for /api specific routes.


@app.errorhandler(404)
@app.errorhandler(405)
def _handle_api_error(ex):
    """ Error handlers for api specific routes

        Error messages will be represented in JSON instead of HTML.
    """
    if request.path.startswith('/api/'):
        message, detail = str(ex).split(": ")
        return jsonify(message=message, detail=detail), ex.code
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
