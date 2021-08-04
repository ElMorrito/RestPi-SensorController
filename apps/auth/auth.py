from flask_security.datastore import SQLAlchemyUserDatastore
from database.database import db
from apps.auth.models import Users, Roles

user_datastore = SQLAlchemyUserDatastore(
    db, Users, Roles)
