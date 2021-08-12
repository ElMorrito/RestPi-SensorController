import os
import tempfile


class Config(object):
    DEBUG = False

    TESTING = False

    CSRF_ENABLED = True

    SECRET_KEY = "57e19ea558d4967a552d03deece34a70"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ADMIN_USERNAME = "Admin"

    ADMIN_PASSWORD = "admin"


class ProductionConfig(Config):

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

    ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD')

    ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME')


class DevelopmentConfig(Config):
    ENV = "development"

    DEVELOPMENT = True

    DEBUG = True

    SQLALCHEMY_DATABASE_URI = "sqlite:///development_database.db"


class TestConfig(Config):

    DEBUG = True

    TESTING = True

    SQLALCHEMY_DATABASE_URI = "sqlite:///test_database.db"
