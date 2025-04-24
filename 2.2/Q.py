# Корень зла

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

a, b, c = float(input()), float(input()), float(input())

if a != 0:  # Квадратическое уравнение
    D = b ** 2 - 4 * a * c
    if D < 0:
        print("No solution")
    elif D >= 0:
        x1 = (-b - D ** 0.5) / (2 * a)
        x2 = (-b + D ** 0.5) / (2 * a)
        x1, x2 = min(x1, x2), max(x1, x2)  # Вывод в порядке возрастания
        if x1 == x2:
            print(round(x1, 2))
        else:
            print(round(x1, 2), round(x2, 2))

elif a == 0:        # Линейное уравнение 
    if b != 0:      # Зависит от x
        x = -c / b  # bx + c = 0  =>  bx = -c
        print(round(x, 2))
    elif b == 0:    # Не зависит от х
        if c == 0:
            print("Infinite solutions")
        elif c != 0:
            print("No solution")
