# Доставка

name = input()
price = int(input())
weight = int(input())
money = int(input())

total = weight * price
back_money = money - total
price_str = str(weight) + "кг * " + str(price) + "руб/кг"

print("=" * 16 + "Чек" + "=" * 16)
print(f"Товар: {name: >28}")
print(f"Цена: {price_str: >29}")
print(f"Итого: {total: >25}руб")
print(f"Внесено: {money: >23}руб")
print(f"Сдача: {back_money: >25}руб")
print("=" * 35)
