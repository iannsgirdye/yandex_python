# Числовой прямоугольник 2.0

N = int(input())
M = int(input())

count = N * M
max_len = len(str(count))

for i in range(1, N + 1):
    for j in range(i, count + 1, N):
        place = ' ' * (max_len - len(str(j)))
        if count - j < N:
            print(place + str(j))
        else:
            print(place + str(j), end=' ')
