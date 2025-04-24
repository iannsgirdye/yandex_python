# Потоковый НОД

import math
import sys


def gcd(numbers):
    print(math.gcd(*numbers))
    

for line in sys.stdin:
    numbers = list(map(int, line.split()))
    gcd(numbers)
