# Валидация имени


class CyrillicError(Exception):
    pass


class CapitalError(Exception):
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
