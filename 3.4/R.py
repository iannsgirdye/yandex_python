# Таблица истинности

from itertools import product
alf = [0, 1]

data = input()
print('a b c f')
for variant in product(alf, repeat=3):
    a, b, c = variant[0], variant[1], variant[2]
    print(*variant, int(eval(data) == 1))
