# Шаг навстречу

import math

x, y = map(float, input().split())      # Декартовы коордитаны
rho, phi = map(float, input().split())  # Полярные координаты

new_x = rho * math.cos(phi)  # Полярный х в декартов
new_y = rho * math.sin(phi)  # Полярный y в декартов

vector = (abs(new_x - x), abs(new_y - y))    # Вектор из (x, y) в (new_x, new_y)
distance = math.hypot(vector[0], vector[1])  # Длина вектора = расстояние
print(distance)
