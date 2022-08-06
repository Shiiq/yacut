import random
import string
from urllib.parse import urljoin

from .models import URL_map

LENGTH = 6
AVAILABLE_SYMBOLS = string.ascii_letters + string.digits
BASE_URL = 'http://localhost:5000'


def get_unique_short_id() -> str:
    unique_short_id = ''.join(random.choices(AVAILABLE_SYMBOLS, k=LENGTH))
    return unique_short_id


def get_short_link(id):
    short_link = urljoin(BASE_URL, id)
    return short_link

def uid_gen() -> str:
    unique_short_id = ''.join(random.choices(AVAILABLE_SYMBOLS, k=LENGTH))
    while URL_map
    yield unique_short_id
