import re
from http import HTTPStatus

from flask import jsonify, request
from sqlalchemy.sql.expression import exists
from werkzeug.exceptions import NotFound

from . import app, db
from .constants import BASE_URL, PATTERN
from .error_handlers import InvalidAPIUsage
from .models import URL_map, get_unique_id


@app.route('/api/id/', methods=['POST'])
def get_unique_short_id():
    """
    Функция для формирования короткой ссылки.
    Параметр 'url' обязательный. Параметр 'custom_id' опциональный.
    """
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')
    original = data['url']
    # Если идентификатор не был введен или поле пустое, то генерируем сами
    if 'custom_id' not in data or not data['custom_id']:
        id = get_unique_id()
    # Если идентификатор был введен, то проверяем
    # используемые символы и длину, и уникальность
    else:
        id = data['custom_id']
        symbols_check = re.fullmatch(PATTERN, id)
        if not symbols_check:
            raise InvalidAPIUsage(
                'Указано недопустимое имя для короткой ссылки'
            )
        if db.session.query(
                exists().where(URL_map.short == id)
        ).scalar():
            raise InvalidAPIUsage(f'Имя "{id}" уже занято.')

    url_map = URL_map(
        original=original,
        short=id
    )
    db.session.add(url_map)
    db.session.commit()

    short_link = url_map.get_short_link(BASE_URL)
    result = dict(
        url=original,
        short_link=short_link
    )
    return jsonify(result), HTTPStatus.CREATED


@app.route('/api/id/<id>/', methods=['GET'])
def get_original_link(id):
    """
    Функция для поиска и отображения полной ссылки по поступившему id.
    """
    try:
        url_map = URL_map.query.filter_by(short=id).first_or_404()
    except NotFound:
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
    url = url_map.original
    result = dict(url=url)
    return jsonify(result), HTTPStatus.OK
