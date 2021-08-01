from flask_security import Security, SQLAlchemyUserDatastore

from apps.security.models import Users, Roles
from database import database

security = Security()

user_datastore = SQLAlchemyUserDatastore(
    database.db, Users, Roles)
