from datetime import datetime
from urllib.parse import urljoin

from . import db


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
