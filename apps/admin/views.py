
from flask import Blueprint
from flask_admin.contrib.sqla import ModelView

from database import models

from apps.admin.models import UserModelView

from database.database import db

admin_bp = Blueprint('admin', __name__, template_folder='templates/admin')
# Register your models for the admin view here
admin_views = [
    UserModelView(models.Users, db.session),
    ModelView(models.Roles, db.session),
    ModelView(models.Sensor, db.session)
]


