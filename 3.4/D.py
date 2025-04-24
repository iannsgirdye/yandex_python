# Словарная ёлка

import itertools

data = input().split()

for i in range(1, len(data)):
    data[i] = ' ' + data[i]

for element in itertools.accumulate(data):
    print(element)
