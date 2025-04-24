# А роза упала на лапу Азора 3.0

N = int(input())

result = 0
for i in range(N):
    el = input()
    for j in range(len(el) // 2):
        if el[j] != el[len(el) - 1 - j]:
            break
    else:
        result += 1
        
print(result)
