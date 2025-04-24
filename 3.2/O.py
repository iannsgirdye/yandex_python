# Двоичная статистика!

numbers = list(map(int, input().split()))  # ввод чисел
result = []  # список словарей

for i in range(len(numbers)):
    statistic = dict()  # словарь со статистикой числа
    number_2 = bin(numbers[i])[2:]
    statistic['digits'] = len(number_2)
    statistic['units'] = number_2.count('1')
    statistic['zeros'] = number_2.count('0')
    result.append(statistic)

print(result)
