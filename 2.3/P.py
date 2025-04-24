# А роза упала на лапу Азора 2.0

n = input()

flag = True
for i in range(len(n) // 2):
    if n[i] != n[len(n) - i - 1]:
        flag = False
        
if flag:
    print('YES')
else:
    print('NO')
