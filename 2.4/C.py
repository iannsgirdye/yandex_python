# Новогоднее настроение

n = int(input())

count = 0
line = 1
for i in range(1, n + 1):
    if count < line - 1:
        print(i, end=' ')
        count += 1
    else:
        print(i)
        count = 0
        line += 1
