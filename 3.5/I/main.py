# Файловая чистка

from itertools import chain

file_in = open(input(), 'r', encoding='UTF-8')  # Открываем первый файл для чтения
data = []  # создаём список для строк
for line in file_in:  # Удаляем передние и задние пробелы, добавляем строку в список
    data.append(line.rstrip(' ').strip(' '))  

data = ''.join(data)  # соединяем все строки в единую строку
while ('\t' in data) or ('  ' in data) or ('\n\n' in data):  # убираем лишние символы, пока они есть
    while '\t' in data:
        data = data.replace('\t', '')
    while '\n\n' in data:
        data = data.replace('\n\n', '\n')
    while '  ' in data:
        data = data.replace('  ', ' ')

file_in.close()  # Закрываем первый файл

file_out = open(input(), 'w', encoding='UTF-8')  # Открываем второй файл для записи
file_out.write(data)  # Записываем результат во второй файл
file_out.close()  # Закрываем второй файл
