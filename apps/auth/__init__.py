from flask_login import LoginManager
from apps.auth import views, models


login_manager = LoginManager()

login_manager.init_app(views.auth_bp)
