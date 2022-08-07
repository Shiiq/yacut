import random
import string
from urllib.parse import urljoin


LENGTH = 6
AVAILABLE_SYMBOLS = string.ascii_letters + string.digits
BASE_URL = 'http://localhost:5000'


def get_short_link(base, id):
    result_link = urljoin(base, id)
    return result_link


# def get_unique_id() -> str:
#     """
#     Генерирует случайный идентификатор
#     :return: id
#     """
#     unique_short_id = ''.join(random.choices(AVAILABLE_SYMBOLS, k=LENGTH))
#     return unique_short_id
# def gen_unique_id(condition) -> str:
#     """
#     Проверяет идентификатор на уникальность, если такой
#     уже существует в БД, то генерирует и возращает новый.
#     :param condition: SQL-условие для проверки
#     :return: id
#     """
#     x = ''.join(random.choices(AVAILABLE_SYMBOLS, k=LENGTH))
#     while condition:
#         x = ''.join(random.choices(AVAILABLE_SYMBOLS, k=LENGTH))
#     return x
#
#
# datab = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def check_uniq():
#     start_x = random.choice(values)
#     x = start_x
#     print('Поступило в функцию =', x)
#     is_exists = x in datab
#     while x in datab:
#         print('Не уникальное значение =', x)
#         x = random.choice(values)
#         print('Перегенерируем х внутри цикла =', x)
#         # return x
#     print('Возвращаем =', x)
#     return x
# def check_uniq(uniq):
#     x = uniq
#     print('Поступило в функцию =', x)
#     while x in datab:
#         print('Не уникальное значение =', x)
#         x = gen_rand()
#         print('Перегенерируем х внутри цикла =', x)
#         # return x
#     print('Возвращаем =', x)
#     return x
# check_uniq()