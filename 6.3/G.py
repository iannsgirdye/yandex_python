# Рассылка сообщений

import requests
import sys

server, user_id = input(), input()              # Ввод элементов url
url = "http://" + server + "/users/" + user_id  # Адрес сервера
data = requests.get(url)                        # Сведения о пользователях

if data.status_code != 404:  # Проверка на то, что пользователь найден
    data = data.json()       # Преобразование данных
    
    message = ""             # Сохранение сообщения
    for line in sys.stdin:
        message += line
        
    print(message.format(    # Форматирование и вывод сообщения
        id=data["id"],
        username=data["username"],
        last_name=data["last_name"],
        first_name=data["first_name"],
        email=data["email"]))
else:
    print("Пользователь не найден")
