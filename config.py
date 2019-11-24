import os


class Config:
    SECRET_KEY='parapon8'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://clyde:parapon8@localhost/pitches'
    UPLOADED_PHOTOS_DEST ='app/static/photos'

#  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'clyde'
    MAIL_PASSWORD = 'parapon8'
    SUBJECT_PREFIX = 'Let The Pitch Out!'
    SENDER_EMAIL = 'clyde.bts17@gmail.com'

    @staticmethod
    def init_app(app):
        pass
    
class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://clyde:parapon8@localhost/pitches'

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://clyde:parapon8@localhost/pitches'


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://clyde:parapon8@localhost/pitches'

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}