# Азбука

N = int(input())
result = 'YES'

for i in range(N):
    line = input()
    if line[0] not in 'абвАБВ':
        result = 'NO'
        
print(result)
