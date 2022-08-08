import random
from datetime import datetime
from urllib.parse import urljoin

from sqlalchemy.sql.expression import exists

from . import db
from .constants import AVAILABLE_SYMBOLS_FOR_ID, ID_LENGTH


class URL_map(db.Model):
    """
    Модель для хранения связки
    оригинальный URL и короткий URL
    """
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(512), unique=True, nullable=False)
    short = db.Column(db.String(16), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def get_short_link(self, base_url):
        """Формирует готовую ссылку из базового URL и идентификатора."""
        short_link = urljoin(base_url, self.short)
        return short_link


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
