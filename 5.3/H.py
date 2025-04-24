# Валидация имени пользователя


class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


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
