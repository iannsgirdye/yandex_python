# Делители


numbers = {1, 2, 3, 4, 5}

result = {num: count for num, count in [(n, [int(x) for x in range(1, n + 1) if n % x == 0]) for n in numbers]}

print(result)