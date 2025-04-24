# Простая задача 2.0

def f(n):
    global all_d
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            all_d.append(d)
            n //= d
            if n > 1:
                f(n)
            break
    else:
        all_d.append(n)
                
                
all_d = []
result = ''
f(int(input()))
for i in all_d:
    if result == '':
        result += str(i)
    else:
        result += ' * ' + str(i)

print(result)
