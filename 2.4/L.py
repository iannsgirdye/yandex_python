# Числовой прямоугольник

N = int(input())
M = int(input())

count = N * M
max_len = len(str(count))
for i in range(1, count + 1):
    place = ' ' * (max_len - len(str(i)))
    if i % M == 0:
        print(place + str(i))
    else:
        print(place + str(i), end=' ')
