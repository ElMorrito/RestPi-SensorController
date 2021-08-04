
from flask import Blueprint
from flask_admin.contrib.sqla import ModelView

from apps.auth.models import Users, Roles
from apps.app.models import Sensor
from apps.admin.models import UserModelView, SensorModelView
from database.database import db

admin_bp = Blueprint(
    'admin_bp', __name__, template_folder='templates')

# Register your models for the admin view here
admin_views = [
    UserModelView(Users, db.session),
    ModelView(Roles, db.session),
    SensorModelView(Sensor, db.session)
]
