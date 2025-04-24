# Простая задача

def f(n):
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True


m = int(input())
if m == 1 or (not f(m)):
    print('NO')
else:
    print('YES')
