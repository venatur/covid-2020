import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = '123456'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database/daily.sqlite3'
    UPLOAD_FOLDER = r'res/'
    DB_FOLDER = 'database'
    EXTENSION = 'csv'
    URL = "http://epidemiologia.salud.gob.mx/gobmx/salud/datos_abiertos/datos_abiertos_covid19.zip"
    ZIP_FILE = "res/covid.zip"


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True