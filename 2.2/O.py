# Властелин чисел: Возвращение Цезаря

number1 = int(input())
number2 = int(input())

a1 = number1 // 10
b1 = number1 % 10
a2 = number2 // 10
b2 = number2 % 10

MAX = max(a1, b1, a2, b2)
MIN = min(a1, b1, a2, b2)
MIDDLE = (a1 + b1 + a2 + b2 - MAX - MIN) % 10

print(str(MAX) + str(MIDDLE) + str(MIN))
