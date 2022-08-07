from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional

MIN_LENGTH = 6
MAX_LENGTH = 16


class ConvertURLForm(FlaskForm):
    original_link = StringField(
        'Оригинальный URL',
        validators=[DataRequired()]
    )
    # дописать кастомный валидатор на основе регулярки
    custom_id = StringField(
        'Желаемый короткий идентификатор',
        validators=[Optional(), Length(MIN_LENGTH, MAX_LENGTH)]
    )
    submit = SubmitField('Сконвертировать')
