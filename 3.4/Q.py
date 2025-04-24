# А есть ещё варианты? | программа не прошла все тесты

from itertools import product, combinations

all_suits = ['бубен', 'пик', 'треф', 'червей']
all_roles = ['10', '2', '3', '4', '5', '6', '7', '8', '9', 'валет', 'дама', 'король', 'туз']

chosen_suit = input()   # Вводим масть, которая должна быть в тройке
chosen_role = input()   # Вводим роль, которой не должно быть в тройке
last_variant = input()  # Вводим последнюю тройку

all_roles.remove(chosen_role)    # Исключаем роль, которой не должно быть в тройке
for i in range(len(all_suits)):  # Запоминаем в нужном падеже масть, которая должна быть в тройке
    if chosen_suit[:2] == all_suits[i][:2]:
        important_suit = all_suits[i]
        break

flag = False  # Для отметки о том, что дошли до прошлой тройки
for variant_of_role in product(all_roles, repeat=3):      # Перебираем все тройки ролей
    for variant_of_suit in product(all_suits, repeat=3):  # Перебираем все тройки мастей
        _1st = variant_of_role[0] + ' ' + variant_of_suit[0]  # 1-я карта
        _2nd = variant_of_role[1] + ' ' + variant_of_suit[1]  # 2-я карта
        _3rd = variant_of_role[2] + ' ' + variant_of_suit[2]  # 3-я карта
        line = _1st + ', ' + _2nd + ', ' + _3rd               # Тройка карт
        if line == last_variant:  # Если тройка равна предыдущей,
            flag = True           # то отмечаем, что следующую подходящую нужно вывести
            continue              # и продолжаем работу программы
        # Если нужная масть есть в тройке и все карты разные
        if all(important_suit in line, _1st != _2nd, _2nd != _3rd, _3rd != _1st):
            if flag:         # и если дошли до предыдущей тройки
                print(line)  # то выводим тройку
                exit()       # и завершаем работу программы
