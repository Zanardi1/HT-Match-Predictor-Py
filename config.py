import os


class Config:
    FLASK_ENV = os.environ.get('FLASK_ENV')
    TESTING = os.environ.get('TESTING')
    DEBUG = os.environ.get('DEBUG')
