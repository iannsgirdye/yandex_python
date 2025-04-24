# Конкретное значение

import requests

url = "http://" + input()  # Адрес сервера
key = input()              # Имя ключа

request = requests.get(url).json()
try:
    print(request[key])
except KeyError:
    print("No data")
