# Рациональная считалочка

from itertools import count

data = list(map(float, input().split()))

for i in count(data[0], data[2]):
    if i <= data[1]:
        print(round(i, 2))
    else:
        break
