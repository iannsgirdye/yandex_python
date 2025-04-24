# Изменение данных

import requests
import sys

server, user_id = input(), input()  # Ввод элементов url

data = dict()                       # Ввод новых данных
for line in sys.stdin:
    line = line.rstrip("\n").split("=")
    data[line[0]] = line[1]

url = "http://" + server + "/users/" + user_id  # Отправка данных
request = requests.put(url=url, json=data)
