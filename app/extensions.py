from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_admin import Admin
from flask_security import Security


db = SQLAlchemy()
ma = Marshmallow()

admin = Admin(name="RestPi-Controller", template_mode='bootstrap4')

security = Security()
