import os


class Config(object):
    DEBUG = False

    TESTING = False

    CSRF_ENABLED = True

    SECRET_KEY = '57e19ea558d4967a552d03deece34a70'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # flask_security config
    SECURITY_REGISTERABLE = True

    SECURITY_PASSWORD_SALT = 'saltyasfuck'


class ProductionConfig(Config):
    DEBUG = False

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class DevelopmentConfig(Config):
    ENV = "development"

    DEVELOPMENT = True

    DEBUG = True

    SQLALCHEMY_DATABASE_URI = "sqlite:///development_database.db"

    SECURITY_SEND_REGISTER_EMAIL = False
