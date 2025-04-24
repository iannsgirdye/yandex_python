# Редизайн таблицы умножения

N = int(input())
M = int(input())
    
for i in range(1, N + 1):
    line = ''
    for j in range(1, N + 1):
        pr = i * j
        spaces = M - len(str(pr))
        spaces_after = '+' * ((spaces // 2) + (spaces % 2))
        spaces -= len(spaces_after)
        spaces_before = '+' * spaces
        line += spaces_before + str(pr) + spaces_after 
        if j + 1 <= N:
            line += '|'
    print(line)
    if i != N:
        print('-' * len(line))
