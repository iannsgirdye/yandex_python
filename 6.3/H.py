# Регистрация нового пользователя

import requests

server = input()
user = {
    "username": input(),
    "last_name": input(),
    "first_name": input(),
    "email": input()
}

url = "http://" + server + "/users"
request = requests.post(url=url, json=user)
