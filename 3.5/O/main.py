# Поставь себя на моё место

import json
import sys

with open('scoring.json', 'r', encoding='UTF-8') as file:
    data = json.load(file)

input_tests = [x.rstrip('\n') for x in sys.stdin]

total = 0        # счётчик суммы баллов
test_index = -1
for i in range(len(data)):                               # Проходимся по группам тестов
    group_points = data[i]["points"]                     # Количество баллов за все правильные тесты группы
    group_tests = len(data[i]["tests"])                  # Количество тестов в группе
    group_points_one_test = group_points // group_tests  # Количество баллов за 1 правильный тест в группе
    
    for test in data[i]["tests"]:                       # Проходимся по тестам в группе
        test_index += 1
        if test["pattern"] == input_tests[test_index]:  # Если результат теста сходится с ответом,
            total += group_points_one_test              # то добавляем в сумме баллов баллы за 1 правильный тест в группе

print(total)  # Выводим сумму баллов