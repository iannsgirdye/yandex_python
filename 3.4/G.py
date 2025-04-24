# Игровая сетка

from itertools import combinations

N = int(input())  # количество учеников
people = [input() for x in range(N)]  # ученики

for pair in combinations(people, 2):
    print(pair[0], '-', pair[1])
