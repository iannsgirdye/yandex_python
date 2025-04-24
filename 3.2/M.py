# Дайте чего-нибудь новенького!

N = int(input())  # число блюд, которые можно приготовить в столовой
variants = [input() for x in range(N)]
variants.sort()

M = int(input())  # число дней, о которых имеется информация
for i in range(M):
    C = int(input())  # число блюд, приготовленных в течение дня
    for j in range(C):
        food = input()
        if food in variants:
            variants.remove(food)

if len(variants) > 0:
    for element in variants:
        print(element)
else:
    print('Готовить нечего')
