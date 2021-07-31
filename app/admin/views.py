
from flask_admin.contrib.sqla import ModelView

from app import models

from app.admin.models import UserModelView

from app.database import db


# Register your models for the admin view here
admin_views = [
    UserModelView(models.Users, db.session),
    ModelView(models.Roles, db.session),
    ModelView(models.Sensor, db.session)
]
