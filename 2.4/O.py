# Числовая змейка 2.0

N = int(input())
M = int(input())

count = N * M
max_len = len(str(count))
raz1 = N * 2 + 1
raz2 = -1
for i in range(1, N + 1):
    spaces = ' ' * (max_len - len(str(i)))
    line = spaces + str(i)
    raz1 -= 2
    raz2 += 2
    last_num = i
    for j in range(2, M + 1):
        line += ' '
        if j % 2 == 0:
            num = last_num + raz1
        else:
            num = last_num + raz2
        spaces = ' ' * (max_len - len(str(num)))
        line += spaces + str(num)
        last_num = num
    print(line)
