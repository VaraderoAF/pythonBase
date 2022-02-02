import os

SQLALCHEMY_DATABASE_URI = os.getenv(
    "SQLALCHEMY_DATABASE_URI",
    "postgresql+psycopg2://car:pwd@localhost:5432/cars",
)


SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "notverysecret",
)


class Config:
    DEBUG = False
    TESTING = False
    ENV = "development"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    SECRET_KEY = SECRET_KEY


class ProductionConfig(Config):
    DEBUG = False
    ENV = "production"


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True