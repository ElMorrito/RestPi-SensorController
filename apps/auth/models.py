from database.database import db
from database.models import BaseModel
from flask_login import UserMixin

# roles_users_table = db.Table('roles_users',
#                              db.Column('users_id', db.Integer(),
#                                        db.ForeignKey('users.id')),
#                              db.Column('roles_id', db.Integer(),
#                                        db.ForeignKey('roles.id')))


class Users(BaseModel, UserMixin):
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean())
    # roles = db.relationship('Roles', secondary=roles_users_table,
    #                         backref='user', lazy=True)


# class Roles(BaseModel, RoleMixin):
#     name = db.Column(db.String(80), unique=True)
#     description = db.Column(db.String(255))

#     def __repr__(self):
#         return '{}'.format(self.name)
