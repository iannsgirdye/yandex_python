# Слияние с проверкой

def merge(first, second):
    try:
        iter(first), iter(second)
    except StopIteration:
        raise StopIteration("Вызвано исключение StopIteration")
    except TypeError:
        raise StopIteration("Вызвано исключение StopIteration")
    
    comprasion = type(first[0])  # Тип, который должен быть у всех элементов
    for i in range(len(first)):
        if not isinstance(first[i], comprasion):
            raise TypeError("Вызвано исключение TypeError")
    for j in range(len(second)):
        if not isinstance(second[j], comprasion):
            raise TypeError("Вызвано исключение TypeError")
     
    first, second = list(first), list(second)
    if (first != sorted(first)) or (second != sorted(second)):
        raise ValueError("Вызвано исключение ValueError")
    
    return tuple(sorted((first + second)))
