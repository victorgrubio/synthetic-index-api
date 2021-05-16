import os


class Config(object):
    DEBUG = False
    TESTING = False
    HOST = '0.0.0.0'
    ORIGINS = '*'
    CORS_SUPPORTS_CREDENTIALS = True
    CORS_ALLOW_HEADERS = 'Content-Type, Authorization'
    CORS_EXPOSE_HEADERS = 'Content-Type, Authorization'

    PORT = 5000
    if os.getenv('API_PORT'):
        PORT = int(os.environ['API_PORT'])

class ProductionConfig(Config):
    BASE_DATABASE_URI = 'root:root@mysql_db:3306/wealth'
    SQLALCHEMY_DATABASE_URI = f'mysql://{BASE_DATABASE_URI}'
    DATABASE_URI= f'mysql+mysqlconnector://{BASE_DATABASE_URI}'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class DevelopmentConfig(Config):
    BASE_DATABASE_URI = 'root:root@mysql_db:3306/wealth'
    SQLALCHEMY_DATABASE_URI = f'mysql://{BASE_DATABASE_URI}'
    DATABASE_URI= f'mysql+mysqlconnector://{BASE_DATABASE_URI}'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True

class TestingConfig(Config):
    BASE_DATABASE_URI = 'root:root@mysql_db:3306/wealth'
    SQLALCHEMY_DATABASE_URI = f'mysql://{BASE_DATABASE_URI}'
    DATABASE_URI= f'mysql+mysqlconnector://{BASE_DATABASE_URI}'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    TESTING = True

