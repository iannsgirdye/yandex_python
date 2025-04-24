# Простая задача 5.0


def is_prime(n):
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True
