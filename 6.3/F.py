# Список пользователей

import requests

url = "http://" + input() + "/users"
data = requests.get(url).json()
users = sorted([data[user]["last_name"] + " " + data[user]["first_name"] for user in range(len(data))])

for user in users:
    print(user)
