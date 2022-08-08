import re

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional, ValidationError

from .constants import MIN_LENGTH, MAX_LENGTH, PATTERN


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
                'Недопустимые символы. Используйте 0-9, a-z, A-Z.'
            )
