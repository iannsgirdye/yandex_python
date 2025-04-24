# Красота спасёт мир

number = int(input())

a = number // 100
b = (number // 10) % 10
c = number % 10

min_abc = min(a, b, c)
max_abc = max(a, b, c)
middle_abc = a + b + c - min_abc - max_abc
if min_abc + max_abc == middle_abc * 2:
    print('YES')
else:
    print('NO')
