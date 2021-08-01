from database.database import db
from database.models import BaseModel
from flask_security import RoleMixin, UserMixin


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

    # def is_accessible(self):
    #     return (current_user.is_active and current_user.is_authenticated)
    # def _handle_view(self, name, **kwargs):
    #     if not self.is_accessible():
    #         return redirect(url_for('security.login'))


class Roles(BaseModel, RoleMixin):
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __repr__(self):
        return '{}'.format(self.name)
