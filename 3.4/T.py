# Таблицы истинности 3 | программа не прошла все тесты

from itertools import product


def create(data, new_data, operator):
    operator_len = len(operator)
    for i in range(len(data) - operator_len + 1):  # Проходимся по всем символам строки
        if data[i:i + operator_len] == operator:   # Если из подряд идущих символов получается,
            if new_data[i - 2].isupper() and new_data[i - 2].isalpha():  # Если перед ' and' переменная,
                new_data[i - 2] = '(' + new_data[i - 2]                  # то открываем скобки 
            else:                                                        # Иначе 
                for j in range(i - 3, -1, -1):                           # ищем открывающуюся скобку
                    if '(' in new_data[j]:                                 # Если нашли,
                        new_data[j] = '(' + new_data[j]                    # то открываем скобки
                        break                                            # и проверяем строку дальше
            
            if new_data[i + 1 + operator_len].isupper() and new_data[i + 1 + operator_len].isalpha():
                new_data[i + 1 + operator_len] += ')'             # Если после 'and ' переменная, то закрываем скобки
            else:                                                 # Иначе
                for k in range(i + 2 + operator_len, len(data)):  # ищем закрывающуюся скобку
                    if ')' in new_data[k]:                          # Если нашли,
                        new_data[k] += ')'                          # то закрываем скобки 
                        break                                       # и проверяем строку дальше
    return new_data


data = input()                                                  # Вводим выражение
upper_letters = sorted(list({x for x in data if x.isupper()}))  # Генерируем отсортированный список переменных
print(' '.join(upper_letters), 'F')   # и выводим заголовок таблицы с этими переменными и обозначением функции

data = data.replace('~', '==')  # Заменяем символы операций на корректные
data = data.replace('^', '!=')
data = data.replace('->', '<=')

# '<=' отвечает за '<=' и '!='
numbers_of_neq = []
number_find = 0
for x in range(len(data) - 1):
    if data[x] + data[x + 1] in '!=_<=':
        number_find += 1
        if data[x] + data[x + 1] == '!=':
            numbers_of_neq.append(number_find)
data = data.replace('!=', '<=')

new_data = list(data)                                 # Копия списка, которую будем редактировать
for i in range(len(data) - 2):                        # Проходимся по всем символам строки
    if data[i] + data[i + 1] + data[i + 2] == 'not':  # Если из 3 подряд идущих символов получается not,
        new_data[i] = '(n'                            # то открываем скобки перед ним
        
        if data[i + 4] == '(':                          # Если после not открывается скобка,
            for j in range(i + 5, len(data)):           # то ищем закрывающуюся скобку
                if data[j] == ')':                        # Если нашли,
                    new_data[j] += ')'                    # то закрываем открытую перед not скобки
                    break                                 # и проверяем строку дальше
        else:                                           # Иначе
            new_data[i + 4] += ')'                      # закрываем скобки после переменной
            
data = ''.join(new_data)
new_data = list(data)

operators = ['and', 'or', '<=']
for k in range(3):
    if operators[k] in data:
        data = ''.join(create(data, new_data, operators[k]))
        new_data = list(data)

number_check = 0
for m in range(len(new_data) - 1):
    if new_data[m] + new_data[m + 1] in '!=_<=':
        number_check += 1
        if number_check in numbers_of_neq:
            new_data[m] = '!'
data = ''.join(new_data)

if '==' in data:
    data = data.split(' == ')
    data = '(' + data[0] + ') == (' + data[1] + ')'

print(data)
exit()

for variant in product([0, 1], repeat=len(upper_letters)):
    connection = dict()                                # Создаём словарь для переменных и их значений
    for i in range(len(upper_letters)):                # Проходимся по переменным
        connection[upper_letters[i]] = variant[i]      # Присваиваем переменным значения
    print(*variant, int(eval(data, connection)))  # Определяем значение функции
