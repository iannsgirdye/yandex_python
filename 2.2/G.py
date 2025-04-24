# А роза упала на лапу Азора

number = int(input())

ab = number // 100
c = (number // 10) % 10
d = number % 10
dc = d * 10 + c

if ab == dc:
    print('YES')
else:
    print('NO')
