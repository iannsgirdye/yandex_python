# Зайка — 8

N = int(input())

total = []
for i in range(N):
    total += input().split()

total = set(total)

for element in total:
    print(element)
