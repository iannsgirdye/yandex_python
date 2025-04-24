# Числовой квадрат

N = int(input())

max_el = N // 2 + N % 2
for i in range(1, N + 1):
    line = ''
    for j in range(1, N + 1):
        if j > 1:
            line += ' '
        num = min(i, j, N - i + 1, N - j + 1)
        spaces = ' ' * (len(str(max_el)) - len(str(num)))
        line += spaces + str(num)
    print(line)
