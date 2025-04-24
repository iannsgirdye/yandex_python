# НОД

def f(n):
    all_d = []
    for d in range(1, int(n ** 0.5) + 1):
        if n % d == 0:
            all_d.append(d)
            if d != (n // d):
                all_d.append(n // d)
    return all_d


good = []
first = int(input())
second = int(input())
for i in f(first):
    for j in f(second):
        if i == j:
            good.append(i)
            
print(max(good))
