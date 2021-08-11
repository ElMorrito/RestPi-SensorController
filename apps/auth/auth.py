

from flask_login import LoginManager
from apps.auth import views
from models import User

login_manager = LoginManager()
login_manager.login_view = 'auth.login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


def init_app(app):

    login_manager.init_app(app)
    app.register_blueprint(views.auth_bp)
