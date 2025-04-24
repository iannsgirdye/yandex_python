# Расстановка спортсменов

from itertools import permutations

N = int(input())  # количество спортсменов
people = sorted([input() for x in range(N)])

for variant in permutations(people):
    print(', '.join(variant))
