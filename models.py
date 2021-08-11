from database.database import db
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer(), primary_key=True)
    date_created = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)
    date_modified = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)


class User(BaseModel, UserMixin):
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean())

    def __init__(self, email, password, is_active=True):
        self.email = email
        self.password = generate_password_hash(password)
        self.is_active = is_active

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def set_password(self, password):
        self.password = generate_password_hash(password)


class Sensor(BaseModel):
    name = db.Column(db.String(255), default="", unique=True)
    sensor_id = db.Column(db.String(255), default="",
                          nullable=False, unique=True)
    sensor_category = db.Column(db.String(255), default="Not specified")

    def __repr__(self):
        return "{}".format(self.sensor_id)
