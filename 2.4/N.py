# Числовая змейка

N = int(input())
M = int(input())

count = N * M
max_len = len(str(count))

for i in range(1, N + 1):
    if i % 2 == 1:
        for j in range((count // N) * i - M + 1, (count // N) * i + 1):
            place = ' ' * (max_len - len(str(j)))
            if j % M == 0:
                print(place + str(j))
            else:
                print(place + str(j), end=' ')
    else:
        for k in range((count // N) * i, (count // N) * i - M, -1):
            place = ' ' * (max_len - len(str(k)))
            if k % M == 1:
                print(place + str(k))
            else:
                print(place + str(k), end=' ')
