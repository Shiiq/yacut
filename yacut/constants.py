import os
import string


SECRET_KEY = os.urandom(32)

# Константа для указания длины id при автогенерации
ID_LENGTH = 6

# Доступные символы для генерации id
AVAILABLE_SYMBOLS_FOR_ID = string.ascii_letters + string.digits
PATTERN = r'[a-zA-Z0-9]{6,16}'

# Базовый адрес приложения
BASE_URL = 'http://localhost:5000'