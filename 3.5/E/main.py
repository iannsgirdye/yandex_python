# А роза упала на лапу Азора 6.0

from sys import stdin

repeat = set()

for line in stdin:
    line = line.rstrip().split()
    for element in line:
        if element.lower() == element.lower()[::-1]:
            repeat.add(element)

print(*sorted(list(repeat)), sep='\n')
