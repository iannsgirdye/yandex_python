# Зайка — 6

N = int(input())
result = 0

for i in range(N):
    result += input().count('зайка')

print(result)
