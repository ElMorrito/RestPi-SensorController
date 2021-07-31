from app.database import db
from datetime import datetime
from flask_security import RoleMixin, UserMixin


class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer(), primary_key=True)
    date_created = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)
    date_modified = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)


class Sensor(BaseModel):
    name = db.Column(db.String(255), default="", unique=True)
    sensor_id = db.Column(db.String(255), default="",
                          nullable=False, unique=True)
    sensor_category = db.Column(db.String(255), default="Not specified")

    def __repr__(self):
        return "{}".format(self.sensor_id)


roles_users_table = db.Table('roles_users',
                             db.Column('users_id', db.Integer(),
                                       db.ForeignKey('users.id')),
                             db.Column('roles_id', db.Integer(),
                                       db.ForeignKey('roles.id')))


class Users(BaseModel, UserMixin):
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean())
    roles = db.relationship('Roles', secondary=roles_users_table,
                            backref='user', lazy=True)


class Roles(BaseModel, RoleMixin):
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __repr__(self):
        return '{}'.format(self.name)
