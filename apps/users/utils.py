from random import choice
from string import hexdigits


def generate_token() -> str:
    token = ''.join([choice(hexdigits) for x in range(4)]).upper()
    return token
