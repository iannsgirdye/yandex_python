# Мы делили апельсин 2.0

from itertools import product

N = int(input())  # количество долек апельсина
counts = [int(x) for x in range(1, N - 1)]

print('А Б В')
for variant in product(counts, repeat=3):
    if sum(variant) == N:
        print(*variant)
