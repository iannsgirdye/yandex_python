# Суммирование ответов

import requests

result = 0     # Накопитель суммы
url = input()  # Адрес

while True:
    request = requests.get("http://" + url)        # Запрос
    number = int(request.content.decode("utf-8"))  # Перевод бинарной записи в привычную
    result += number
    if number == 0:
        print(result)
        break
