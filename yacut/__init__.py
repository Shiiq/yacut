import os
import random
import string

from flask import Flask, abort, flash, redirect, render_template, jsonify, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import exists

SECRET_KEY = os.urandom(32)

# Константа для указания длины id при автогенерации
ID_LENGTH = 6

# Доступные символы для генерации id
AVAILABLE_SYMBOLS_FOR_ID = string.ascii_letters + string.digits

# Базовый адрес приложения
BASE_URL = 'http://localhost:5000'

# Параметры приложения
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from .forms import ConvertURLForm
from .models import URL_map
from .utils import get_short_link
from .error_handlers import page_not_found, InvalidAPIUsage


def check_unique_id() -> str:
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


@app.route('/', methods=['GET', 'POST'])
def get_unique_short_id():
    form = ConvertURLForm()
    if form.validate_on_submit():
        original_link = form.original_link.data

        if not form.custom_id.data:
            id = check_unique_id()

        else:
            id = form.custom_id.data

            if db.session.query(
                    exists().where(URL_map.short == id)
            ).scalar():
                flash(
                    'Такой идентификатор уже есть в базе! Придумайте другой.', 'Fault'
                )
                return render_template('main.html', form=form)

        url_map = URL_map(
            original=original_link,
            short=id
        )
        db.session.add(url_map)
        db.session.commit()

        # Вывод сообщения с готовой короткой ссылкой
        short_link = get_short_link(BASE_URL, id)
        flash(short_link, 'Success')

    return render_template('main.html', form=form)


@app.route('/<id>', methods=['GET'])
def redirect_to_original_link(id):
    url_map = URL_map.query.filter_by(short=id).first()
    if url_map is None:
        abort(404)
    original_link = url_map.original
    return redirect(original_link)


@app.route('/api/id/', methods=['POST'])
def get_unique_short_id_api():
    # {
    #     "url": "string",
    #     "custom_id": "string"
    # }

    data = request.get_json()

    if 'url' not in data:
        raise InvalidAPIUsage('Вы забыли указать ссылку.')
    original = data['url']

    # if

    if 'custom_id' not in data:
        id = check_unique_id()
    else:
        id = data['custom_id']
        if db.session.query(
                exists().where(URL_map.short == id)
        ).scalar():
            raise InvalidAPIUsage(
                'Такой идентификатор уже есть в базе! Придумайте другой.'
            )

    short_link = get_short_link(BASE_URL, id)
    url_map = URL_map(
        original=original,
        short=short_link
    )
    db.session.add(url_map)
    db.session.commit()
    return jsonify(url_map.to_dict()), 201

