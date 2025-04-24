# Частная собственность

N = int(input())  # Количество детей в группе

all_toys = []                                                    # Список для всех игрушек
child = input()                                                  # Ввод информации о 0-м ребёнке
all_toys += list(set(child[child.index(':') + 2:].split(', ')))  # Добавление в список игрушек 0-го ребёнка

for i in range(1, N):                                                # Обработка информации об остальных детях
    child = input()                                                  # Ввод информации о следующем ребёнке
    all_toys += list(set(child[child.index(':') + 2:].split(', ')))  # Добавление в список игрушек следующего ребёнка
    
good_toys = []                    # Список для неповторяющихся игрушек
for toy in all_toys:              # Проходим по списку всех игрушек
    if all_toys.count(toy) == 1:  # Если игрушка не повторяется
        good_toys.append(toy)     # то добавляем её в список неповторяющихся игрушек

for good_toy in sorted(good_toys):  # Вывод неповторяющихся игрушек
    print(good_toy)
