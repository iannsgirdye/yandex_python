# Числовой прямоугольник 3.0

from itertools import product

N, M = int(input()), int(input())  # высота, ширина

maxLen = len(str(N * M))
for x in product([int(n) for n in range(1, N + 1)], [int(m) for m in range(1, M + 1)]):
    number = str(x[1] + (x[0] - 1) * M)
    number_out = ' ' * (maxLen - len(number)) + number
    if x[1] < M:
        print(number_out, end=' ')
    else:
        print(number_out)