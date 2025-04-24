# Валидация пароля | программа не прошла все тесты

import string
import hashlib
possible_chars = string.ascii_letters + string.digits


class MinLenghtError(Exception):
    pass


class PossibleCharError(Exception):
    pass


class NeedCharError(Exception):
    pass


def password_validation(password, min_length=8, possible_chars=possible_chars, at_least_one=str.isdigit):
    if not (type(password) is str):
        raise TypeError
    
    if len(password) < min_length:
        raise MinLenghtError
    
    for element in password:
        if element not in possible_chars:
            raise PossibleCharError
    
    if True not in map(at_least_one, password):
        raise NeedCharError
    
    return hashlib.sha256(password.encode()).hexdigest()


print(password_validation(
    "$uNri$e_777",
    min_length=6,
    at_least_one=lambda char: char in "!@#$%^&*()_"
))
