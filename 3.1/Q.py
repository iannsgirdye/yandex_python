# А роза упала на лапу Азора 5.0

string = ''.join(input().lower().split())

for i in range(len(string)):
    if string[i] == string[len(string) - 1 - i]:
        continue
    else:
        print('NO')
        break
else:
    print('YES')
