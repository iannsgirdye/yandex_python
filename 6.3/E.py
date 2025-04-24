# Суммирование ответов 3

import requests
import sys

result = 0  # Накопитель сум элементов списков

server = input()        # Адрес сервера
for path in sys.stdin:  # Запрос данных 
    request = requests.get("http://" + server + path.rstrip("\n"))
    result += sum(request.json())
    
print(result)
