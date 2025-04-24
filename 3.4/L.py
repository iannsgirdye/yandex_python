# Список покупок 2.0

from itertools import chain

N = int(input())  # количество членов семьи
food = sorted(list(chain.from_iterable([input().split(', ') for x in range(N)])))  # единый список еды

for number, value in enumerate(food, 1):
    print(str(number) + '.', value)
