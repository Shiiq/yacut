import re

from flask import jsonify, request
from sqlalchemy.sql.expression import exists

from . import app, db, get_unique_id
from .constants import BASE_URL, PATTERN
from .error_handlers import InvalidAPIUsage
from .models import URL_map


@app.route('/api/id/', methods=['POST'])
def get_unique_short_id_api():
    data = request.get_json()

    if 'url' not in data:
        raise InvalidAPIUsage('Вы забыли указать ссылку.')
    original = data['url']

    if 'custom_id' not in data:
        id = get_unique_id()
    else:
        id = data['custom_id']
        check = re.fullmatch(PATTERN, id)
        if db.session.query(
                exists().where(URL_map.short == id)
        ).scalar() or not check:
            raise InvalidAPIUsage(
                'Недопустимый идентификатор! Придумайте другой.'
            )

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
    return jsonify(result), 201


@app.route('/api/id/<id>/', methods=['GET'])
def get_original_link(id):
    url_map = URL_map.query.filter_by(short=id).first()
    if url_map is None:
        raise InvalidAPIUsage('Такого идентификатора нет в базе данных.', 404)
    url = url_map.original
    result = dict(url=url)
    return jsonify(result), 200
