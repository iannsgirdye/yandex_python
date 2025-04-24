# Зайка — 5

N = int(input())

result = 0
for i in range(N):
    flag = False
    while (line := input()) != 'ВСЁ':
        if line == 'зайка' and (not flag):
            result += 1
            flag = True
        
print(result)
