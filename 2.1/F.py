# Чек

name, price, weight, money_in = input(), int(input()), int(input()), int(input())
total_price = weight * price
money_back = money_in - total_price
print("Чек")
print(f"{name} - {weight}кг - {price}руб/кг")
print(f"Итого: {total_price}руб")
print(f"Внесено: {money_in}руб")
print(f"Сдача: {money_back}руб")
