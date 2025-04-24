# Функциональный НОД

def gcd(x, y):
    return max(Del(x).intersection(Del(y)))


def Del(n):
    all_del = set()
    for d in range(1, int(n ** 0.5) + 1):
        if n % d == 0:
            all_del.add(d)
            if (n // d) != d:
                all_del.add(n // d)
    return all_del
