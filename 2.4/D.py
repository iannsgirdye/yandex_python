# Суммарная сумма

steps = int(input())

result = 0
for i in range(steps):
    n = int(input())
    while n > 0:
        result += n % 10
        n //= 10

print(result)
