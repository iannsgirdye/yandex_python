# А роза упала на лапу Азора 4.0

string = input()

for i in range(len(string)):
    if string[i] == string[len(string) - 1 - i]:
        continue
    else:
        print('NO')
        break
else:
    print('YES')
