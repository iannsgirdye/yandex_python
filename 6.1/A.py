# Математика — круто, но это не точно

import math


x = float(input())
summand1 = math.log(math.pow(x, 3 / 16), 32)
summand2 = math.pow(x, math.cos((math.pi * x) / (2 * math.e)))
summand3 = math.pow(math.sin(x / math.pi), 2)
print(summand1 + summand2 - summand3)
