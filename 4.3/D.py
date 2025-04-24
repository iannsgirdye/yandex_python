# Декор результата


def answer(function):
    string = 'Результат функции: '

    def decorated(*args, **kwargs):
        nonlocal string
        return string + str(function(*args, **kwargs))
    return decorated
