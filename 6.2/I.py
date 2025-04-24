# Бесконечный морской бой

import pandas as pd


x_left, y_left = map(int, input().split())    # верхний левый угол
x_right, y_right = map(int, input().split())  # нижний правый угол

data = pd.read_csv("data.csv")  # импорт таблицы
print(data[(x_left <= data["x"]) & (data["x"] <= x_right) & (y_right <= data["y"]) & (data["y"] <= y_left)])
