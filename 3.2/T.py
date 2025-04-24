# Простая задача 4.0

def f(n):
    all_del = [n]
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            all_del.append(d)
            if (n // d) != d:
                all_del.append(n // d)
    return all_del


numbers = sorted(set(map(int, input().split('; '))))  # Ввод чисел
result = dict()

for i in numbers:
    del_i = f(i)
    for j in numbers:
        if i != j:
            del_j = f(j)
            if len(set(del_i + del_j)) == len(del_i) + len(del_j):
                result[i] = result.get(i, []) + [j]

for key, value in result.items():
    print(key, '-', end=' ')
    print(*value, sep=', ')
