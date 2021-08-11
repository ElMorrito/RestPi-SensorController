
from models import Sensor
from models import User
from flask_admin import Admin
from database.database import db
from apps.admin.views import UserModelView, SensorModelView

# Models for the admin view here
admin_views = [
    UserModelView(User, db.session, name="Users"),
    SensorModelView(Sensor, db.session, name="Sensors")
]

admin = Admin(name="Restpi-Admin", template_mode='bootstrap4')


def init_app(app):

    admin.add_views(*admin_views)

    admin.init_app(app=app)
