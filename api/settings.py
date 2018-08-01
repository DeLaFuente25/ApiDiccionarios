import os


class Config(object):
    SECRET_KEY = 'my_secret_key'


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:alexis@190.114.253.121/flask'
    SQLALCHEMY_MIGRATE_REPO = '/migrations'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
