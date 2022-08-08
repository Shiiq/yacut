import re
import random
import string
from urllib.parse import urljoin


LENGTH = 6
AVAILABLE_SYMBOLS = string.ascii_letters + string.digits
BASE_URL = 'http://localhost:5000'


def get_short_link(base, id):
    result_link = urljoin(base, id)
    return result_link

pattern = r'[a-zA-Z0-9]{6,16}'
short_id_1= 'SjtoQQ'
short_id_2 = 'Sjtxao23Q'
short_id_3 = 'SjtoQQ*'
short_id_4 = 'SjtoQQSjtoQQSjtoQQSjtoQ123Q'
x = re.fullmatch(pattern, short_id_4)
