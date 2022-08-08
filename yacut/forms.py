import re

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional, ValidationError

MIN_LENGTH = 6
MAX_LENGTH = 16
PATTERN = r'[a-zA-Z0-9]{6,16}'


class ConvertURLForm(FlaskForm):
    original_link = StringField(
        'Оригинальный URL',
        validators=[DataRequired()]
    )
    custom_id = StringField(
        'Желаемый короткий идентификатор',
        validators=[Optional(), Length(MIN_LENGTH, MAX_LENGTH)]
    )
    submit = SubmitField('Сконвертировать')

    def validate_custom_id(self, custom_id):
        """Валидация используемых символов при ручном вводе id."""
        check = re.fullmatch(PATTERN, custom_id.data)
        if not check:
            raise ValidationError(
                'Недопустимые символы, используйте 0-9, a-z, A-Z.'
            )
