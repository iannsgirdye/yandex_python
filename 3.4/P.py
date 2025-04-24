# Расклад таков...

from itertools import product

all_suits = ['бубен', 'пик', 'треф', 'червей']
all_roles = ['10', '2', '3', '4', '5', '6', '7', '8', '9', 'валет', 'дама', 'король', 'туз']

chosen_suit = input()  # Вводим масть, которая должна быть в тройке
chosen_role = input()  # Вводим роль, которой не должно быть в тройке

all_roles.remove(chosen_role)    # Исключаем роль, которой не должно быть в тройке
for i in range(len(all_suits)):  # Запоминаем в нужном падеже масть, которая должна быть в тройке
    if chosen_suit[:2] == all_suits[i][:2]:
        important_suit = all_suits[i]
        break

count = 0  # Счётчик количества выведенных троек
for variant in product(all_roles, all_suits, repeat=3):  # Перебираем все возможные варианты троек
    _1st = variant[0] + ' ' + variant[1]                 # 1-я карта
    _2nd = variant[2] + ' ' + variant[3]                 # 2-я карта
    _3rd = variant[4] + ' ' + variant[5]                 # 3-я карта
    line = _1st + ', ' + _2nd + ', ' + _3rd              # Тройка карт
    # Если нужная масть есть в тройке и все карты разные
    if (important_suit in line) and (_1st != _2nd) and (_2nd != _3rd) and (_3rd != _1st):
        print(line)      # то выводим тройку
        count += 1       # Добавляем к количеству выведенных троек единицу
        if count == 10:  # Если вывели 10 троек,
            exit()       # то завершаем работу программы
