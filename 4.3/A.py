# Рекурсивный сумматор


def recursive_sum(*numbers):
    if len(numbers) == 0:
        return 0
    return recursive_sum(*numbers[:-1]) + numbers[-1]
