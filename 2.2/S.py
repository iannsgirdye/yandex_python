# Автомазитация безопасности

x = float(input())
y = float(input())

bad = 'Опасность! Покиньте зону как можно скорее!'
good = 'Зона безопасна. Продолжайте работу.'
water = 'Вы вышли в море и рискуете быть съеденным акулой!'

if x ** 2 + y ** 2 > 10 ** 2:
    print(water)
elif x >= 0 and y >= 0:
    if x ** 2 + y ** 2 <= 5 ** 2:
        print(bad)
elif -4 <= x < 0 and 5 >= y >= 0:
    print(bad)
elif -7 <= x < -4 and 5 >= y >= 0:
    if 5 * x + 35 <= 3 * y:
        print(bad)
elif y < 0:
    if 0.25 * x ** 2 + 0.5 * x - 8.75 <= y:
        print(bad)
else:
    print(good)
