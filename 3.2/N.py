# Это будет шедевр!

N = int(input())                        # Число продуктов в наличии
products = [input() for x in range(N)]  # Названия продуктов в наличии

M = int(input())  # Число рецептов, о которых есть информация
recipes = dict()  # Словарь рецептов, о которых есть информация

for i in range(M):
    name = input()                                            # Название блюда
    count_products = int(input())                             # Количество ингредиентов
    recipes[name] = [input() for y in range(count_products)]  # Необходимые ингредиенты

recipes = dict(sorted(recipes.items()))
flag = True
for name_recipe, list_ingredients in recipes.items():  # Проходимся по названиям блюд и их спискам ингредиентов
    for ingredient in list_ingredients:                # Проходимся по каждому ингредиенту в списке ингредиентов
        if ingredient not in products:                 # Если ингредиент не в списке продуктов,
            break                                      # то переходим к проверке следующего рецепта
    else:                                              # Если все ингредиенты есть в списке продуктов,
        print(name_recipe)                             # то выводим название блюда
        flag = False                                   # и помечаем, что хотя бы одно блюдо можно приготовить
        
if flag:                                               # Если ни одно блюдо нельзя приготовить
    print('Готовить нечего')                           # то выводим строку
