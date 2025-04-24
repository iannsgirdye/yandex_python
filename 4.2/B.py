# Генератор матриц


def make_matrix(size, value=0):
    if type(size) is tuple:
        m, n = size[1], size[0]
    else:
        m = n = size
    return [[value for i in range(n)] for j in range(m)]
