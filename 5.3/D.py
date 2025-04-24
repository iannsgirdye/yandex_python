# Контроль параметров

def only_positive_even_sum(a, b):
    if (not (type(a) is int)) or (not (type(b) is int)):
        raise TypeError("Вызвано исключение TypeError")
    elif (not (a > 0 and a % 2 == 0)) or (not (b > 0 and b % 2 == 0)):
        raise ValueError("Вызвано исключение ValueError")
    else:
        return a + b
