# Валидация пользователя


class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


def name_validation(name):
    if not (type(name) is str):
        raise TypeError
    
    cyrillic = "йцукенгшщзхъэждлорпавыфячсмитьбюё"
    for letter in name.lower():
        if letter not in cyrillic:
            raise CyrillicError
    
    if not name.istitle():
        raise CapitalError
    
    return name


def username_validation(name):
    if not (type(name) is str):
        raise TypeError
    
    alphabet = "qwertyuioplkjhgfdsazxcvbnm1234567890_"
    for letter in name.lower():
        if letter not in alphabet:
            raise BadCharacterError
        
    if name[0].isdigit():
        raise StartsWithDigitError
    
    return name


def user_validation(last_name=None, first_name=None, username=None, *args, **kwargs):
    if (len(args) > 0) or (len(kwargs) > 0):  # Позиционных аргументов быть не должно
        raise KeyError                        # и ненужных именнованых тоже
    
    if not all(type(element) is str for element in (last_name, first_name, username)):
        raise TypeError
    
    name_validation(last_name)
    name_validation(first_name)
    username_validation(username)
    
    return {"last_name": last_name, "first_name": first_name, "username": username}
