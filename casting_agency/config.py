import os

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.

# Enable debug mode.
DEBUG = True


class BaseConfig(object):
    """ Base configuration. """
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL_NEW')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DefaultConfig(BaseConfig):
    DEBUG = False


class DevConfig(BaseConfig):
    DEBUG = True
