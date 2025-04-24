# Простая задача 3.0

def f(n):
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True


result = 0
N = int(input())
for i in range(N):
    num = int(input())
    if f(num) and (num != 1):
        result += 1
        
print(result)
