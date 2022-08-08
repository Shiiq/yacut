import string


# Константа для указания длины id при автогенерации
ID_LENGTH = 6

# Константы для указания максимальной и минимальной длины id
MIN_LENGTH = 1
MAX_LENGTH = 16

# Доступные символы для генерации id (a-z A-Z 0-9)
AVAILABLE_SYMBOLS_FOR_ID = string.ascii_letters + string.digits
PATTERN = r'[a-zA-Z0-9]{1,16}'

# Базовый адрес приложения
BASE_URL = 'http://localhost'