# Удаление данных

import requests

server, user_id = input(), input()
url = "http://" + server + "/users/" + user_id
request = requests.delete(url)
