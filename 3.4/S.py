# Таблица истинности 2

from itertools import product

data = input()  # Ввод логического выражения

# Создание сортированного списка после множества из заглавных букв логического выражения
upper_letters = sorted(list({x for x in data if x.isupper()}))

alf = [0, 1]
print(' '.join(upper_letters), 'F')  # Вывод первой строки таблицы
for variant in product(alf, repeat=len(upper_letters)):  # Генерирование всех возможных значений в таблице 
    connection = dict()  # Создание словаря для соотношения значений и переменных
    for i in range(len(upper_letters)):
        connection[upper_letters[i]] = variant[i]  # Присвоение переменной значения
    print(*variant, int(eval(data, connection) == 1))  # Определение значения функции
