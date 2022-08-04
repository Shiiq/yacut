# from datetime import datetime
#
# # from main import db
# from yacut import db
#
#
# class URL_map(db.Model):
#     """
#     Модель для хранения связки
#     оригинальный URL -> короткий URL
#     """
#     id = db.Column(db.Integer, primary_key=True)
#     original = db.Column(db.String(512), unique=True, nullable=False)
#     short = db.Column(db.String(512), unique=True, nullable=False)
#     timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
