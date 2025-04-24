# НОД 2.0

import math
N = int(input())

nums = [int(input()) for x in range(N)]
results = []

for i in range(N):
    for j in range(i + 1, N):
        results.append(math.gcd(nums[i], nums[j]))

print(min(results))
