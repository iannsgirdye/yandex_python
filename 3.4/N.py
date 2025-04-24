# Спортивные гадания

from itertools import permutations

N = int(input())  # количество спортсменов
people = sorted([input() for x in range(N)])  # Список спортсменов

for variant in permutations(people, 3):
    print(', '.join(variant))
