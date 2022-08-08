import os
from dotenv import load_dotenv

load_dotenv()


class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_secret_key')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
