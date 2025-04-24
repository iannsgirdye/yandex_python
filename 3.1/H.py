# Зайка — 7

N = int(input())

for i in range(N):
    line = input()
    if 'зайка' in line:
        print(line.index('зайка') + 1)
    else:
        print('Заек нет =(')
