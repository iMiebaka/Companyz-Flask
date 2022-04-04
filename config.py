
class Config(object):
    APP_NAME = 'Companyz'

class Development(Config):
    DEBUG = True
    DATABASE_URI = "localhost", 27017

class Production(Config):
    DEBUG = False


config = {
    'development': Development,
    'production': Production,
    'default': Development
}