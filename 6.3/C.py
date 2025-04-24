# Суммирование ответов 2

import requests

result = 0                                   # Накопитель суммы
request = requests.get("http://" + input())  # Запрос по адресу
request = request.json()                     # Преобразование в формат JSON 

for element in request:
    if type(element) is int:
        result += element
        
print(result)
