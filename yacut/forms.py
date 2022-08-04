from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

AVAILABLE_SYMBOLS = ''


class ConvertURLForm(FlaskForm):
    original_link = StringField(
        'Вставьте ссылку, которую нужно сократить',
        # validators=[DataRequired(message='Обязательное поле'), ]
    )
    short_link = StringField(
        'Впишите желаемый идентификатор для ссылки'
        '(большие и маленькие латинские буквы, цифры 0-9),'
        'длина не должна превышать 6 символов',
        # дописать кастомный валидатор на основе регулярки
        # validators=[Length(6, 6, message='Длина идентификатора не должна превышать 6 символов'), ]
    )
    submit = SubmitField('Сконвертировать')
