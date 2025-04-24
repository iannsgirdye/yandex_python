# Генератор Фибоначчи

def fibonacci(n):
    n_0, n_1 = 0, 1
    for i in range(n):
        if i == 0:
            yield n_0
        elif i == 1:
            yield n_1
        else:
            n_2 = n_0 + n_1
            yield n_2
            n_0, n_1 = n_1, n_2
