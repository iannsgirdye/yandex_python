# Меню питания

n = int(input())
food = ['Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая']

for i in range(n):
    print(food[i % 5])
