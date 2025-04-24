# Проверка системы

import requests

request = requests.get("http://127.0.0.1:5000")
message = request.content.decode("utf-8")
print(message)
