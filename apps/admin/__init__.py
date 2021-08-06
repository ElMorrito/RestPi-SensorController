from apps.auth.models import Users
from apps.app.models import Sensor
from apps.admin.models import UserModelView, SensorModelView, SecureModelView
from database.database import db

from flask_admin import Admin


# Models for the admin view here
admin_views = [
    UserModelView(Users, db.session),
    # SecureModelView(Roles, db.session),
    SensorModelView(Sensor, db.session, name='Sensors')
]

admin = Admin(name="Restpi-Admin",
              template_mode='bootstrap4')

admin.add_views(*admin_views)
