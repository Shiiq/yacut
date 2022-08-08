import re
import random
import string

from flask import Flask, abort, flash, redirect, render_template, jsonify, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import exists

from .constants import *


# Параметры приложения
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import api_views, error_handlers, views
# from .forms import ConvertURLForm
from .models import URL_map
# from .utils import get_short_link
# from .error_handlers import page_not_found, InvalidAPIUsage


def get_unique_id():
    """
    Генерирует уникальный идентификатор с проверкой
    уже существующих идентификаторов.
    """
    start_id = ''.join(
        random.choices(AVAILABLE_SYMBOLS_FOR_ID, k=ID_LENGTH)
    )
    id = start_id
    while db.session.query(exists().where(URL_map.short == id)).scalar():
        id = ''.join(
        random.choices(AVAILABLE_SYMBOLS_FOR_ID, k=ID_LENGTH)
    )
    return id
