# Список покупок 3.0

from itertools import chain, permutations

N = int(input())  # количество членов семьи
food = sorted(list(chain.from_iterable([input().split(', ') for n in range(N)])))

for variant in permutations(food, 3):
    print(*variant)
