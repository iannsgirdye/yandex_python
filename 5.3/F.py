# Корень зла 2

"""
Квадратичное уравнение (a != 0):
  • D  > 0: 2 решения
  • D == 0: 1 решение
  • D <  0: 0 решений    

Линейное уравнение (a == 0):
  • b == 0:
    • c == 0: infinity решений
    • c != 0: 0 решений
  • b != 0: 1 решение
"""


class NoSolutionsError(Exception):
    pass


class InfiniteSolutionsError(Exception):
    pass


def find_roots(a, b, c):
    for element in (a, b, c):
        if (type(element) is int) or (type(element) is float):
            continue
        raise TypeError("Вызвано исключение TypeError")
    
    if a != 0:  # Квадратическое уравнение
        D = b ** 2 - 4 * a * c
        if D < 0:
            raise NoSolutionsError("Вызвано исключение NoSolutionsError")
        elif D >= 0:
            x1 = (-b - D ** 0.5) / (2 * a)
            x2 = (-b + D ** 0.5) / (2 * a)
            x1, x2 = min(x1, x2), max(x1, x2)  # Вывод в порядке возрастания
            return x1, x2

    elif a == 0:        # Линейное уравнение 
        if b != 0:      # Зависит от x
            x = -c / b  # bx + c = 0  =>  bx = -c
            return x
        elif b == 0:    # Не зависит от х
            if c == 0:
                raise InfiniteSolutionsError("Вызвано исключение InfiniteSolutionsError")
            elif c != 0:
                raise NoSolutionsError("Вызвано исключение NoSolutionsError")
