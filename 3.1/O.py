# НОД 3.0

import math

numbers = list(map(int, input().split()))

result = math.gcd(numbers[0], numbers[1])
for i in range(2, len(numbers)):
    result = math.gcd(result, numbers[i])
    
print(result)
