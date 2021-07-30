from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_admin import Admin
from flask_security import Security
import os

db = SQLAlchemy()
ma = Marshmallow()

security = Security()
