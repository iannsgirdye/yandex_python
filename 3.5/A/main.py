# A+B+...

from sys import stdin
from itertools import chain

data = []

for line in stdin:
    data.append(list(map(int, line.rstrip().split())))

print(sum(list(chain.from_iterable(data))))
