
from flask import Blueprint
from flask_admin.contrib.sqla import ModelView

from apps.security.models import Users, Roles
from apps.app.models import Sensor
from apps.admin.models import UserModelView
from database.database import db

admin_bp = Blueprint('admin', __name__, template_folder='templates/admin')
# Register your models for the admin view here

admin_views = [
    UserModelView(Users, db.session),
    ModelView(Roles, db.session),
    ModelView(Sensor, db.session)
]
