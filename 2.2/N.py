# Властелин Чисел: Две Башни

number = int(input())

a = number // 100
b = (number // 10) % 10
c = number % 10

MAX = max(a, b, c)
MIN = min(a, b, c)
MIDDLE = a + b + c - MAX - MIN

if MIN == 0 and MIDDLE == 0:
    print(str(MAX) + str(MIN), str(MAX) + str(MIN))
elif MIN == 0 and MIDDLE != 0:
    print(str(MIDDLE) + str(MIN), str(MAX) + str(MIDDLE))
else:
    print(str(MIN) + str(MIDDLE), str(MAX) + str(MIDDLE))
