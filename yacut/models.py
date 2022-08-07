from datetime import datetime

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

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=self.short
        )
