# Файловая статистика

file_name = input()

file = open(file_name, 'r', encoding='UTF-8')
data = list(map(int, file.read().split()))
file.close()

print(len(data))  # количество всех чисел
print(len([number for number in data if number > 0]))  # количество положительных чисел
print(min(data))  # минимальное число
print(max(data))  # максимальное число
print(sum(data))  # сумма всех чисел
print(round(sum(data) / len(data), 2))
