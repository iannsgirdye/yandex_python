# Таблица умножения 3.0

from itertools import product

n = int(input())
numbers = [int(x) for x in range(1, n + 1)]

for total in product(numbers, repeat=2):
    if total[1] == n:
        print(total[0] * total[1])
    else:
        print(total[0] * total[1], end=' ')
