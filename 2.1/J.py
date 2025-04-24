# Деловая колбаса

name, number = input(), int(input())
first, second, third = number // 100, (number // 10) % 10, number % 10
print(f"Группа №{first}.", f"{third}. {name}.", f"Шкафчик: {number}.", f"Кроватка: {second}.", sep="\n")
