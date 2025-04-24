# Меню питания 2.0

from itertools import cycle

M = int(input())  # количество каш в меню
food = [input() for x in range(M)]  # список каш
N = int(input())  # количество дней

for element in cycle(food):
    print(element)
    N -= 1
    if N == 0:
        break
