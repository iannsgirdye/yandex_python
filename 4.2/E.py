# Подготовка данных


def to_string(*data, sep=' ', end='\n'):
    data = list(map(str, data))
    return sep.join(data) + end
    