# Карта сокровищ

N = int(input())       # Количество точек
dots = dict()          # Словарь точек по категориям

for i in range(N):
    x, y = input().split()  # Считываем координаты точки
    # Формируем ключ для словаря точек: 1-я цифра 1-го (числа) + 1-я цифра 2-го + длина 1-го + длина 2-го
    category = x[:-1] + y[:-1] + str(len(x)) + str(len(y))
    dots[category] = dots.get(category, 0) + 1  # Добавляем к значению по ключу единицу

print(max(dots.values()))  # Определяем максимальное значение и выводим его
