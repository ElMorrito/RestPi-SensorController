
from models import Sensors
from models import Users
from flask_admin import Admin
from database.database import db
from apps.admin.views import UserModelView, SensorModelView, SecureModelView

# Models for the admin view here
admin_views = [
    UserModelView(Users, db.session),
    SensorModelView(Sensors, db.session, name='Sensors')
]
admin = Admin(name="Restpi-Admin", template_mode='bootstrap4')


def init_app(app):

    admin.add_views(*admin_views)

    admin.init_app(app=app)
