# Слияние данных | программа не прошла все тесты

from json import load, dump

file_users_name = input()    # Вводим имя файла с информацией о пользователях
file_updates_name = input()  # Вводим имя файла с обновлённой информацией о пользователях

with open(file_users_name, 'r', encoding='UTF-8') as file_users:  # Считываем информацию с файлов
    file_users_data = load(file_users)

with open(file_updates_name, 'r', encoding='UTF-8') as file_updates:
    file_updates_data = load(file_updates)

new_data = dict()  # Создаём словарь, который сформируем по условию задания
for i in range(len(file_users_data)):  # Проходимся по каждому словарю файла
    name = file_users_data[i]["name"]  # Сохраняем ключ-имя для будущего
    new_data[name] = dict()            # Создаём словарь-значение по ключу-имени человека
    del file_users_data[i]["name"]     # Удаляем ключ-имя из старого словаря (для удобства)
    del file_updates_data[i]["name"]   # Удаляем ключ-имя из словаря с изменениями (-//-)
    
    for old_info in file_users_data[i]:       # Проходимся по старым ключам
        if old_info in file_updates_data[i]:  # Если ключ есть в обновлении, то присваиваем большее значение
            new_data[name][old_info] = max(file_users_data[i][old_info], file_updates_data[i][old_info])
        else:                                 # Иначе добавляем новый дополнительный параметр
            new_data[name][old_info] = file_users_data[i][old_info]
    for new_info in file_updates_data[i]:       # Проходимся по обновлённым ключам
        if new_info not in file_users_data[i]:  # Если ключа нет среди старых, то добавляем его
            new_data[name][new_info] = file_updates_data[i][new_info]
    
with open(file_users_name, 'w', encoding='UTF-8') as file_users:
    dump(new_data, file_users, ensure_ascii=False, indent=4)
