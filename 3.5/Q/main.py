# Прятки

with open('secret.txt', 'r', encoding='UTF-8') as file:  # Открываем файл
    file_data = file.read()                                                # и считываем данные

new_data = ''  # Создаём строку для добавления в неё полученных символов
for letter in file_data:               # Проходимся по каждому символу входных данных
    letter_ord = ord(letter)           # Вычисляем код символа
    letter_ord2 = bin(letter_ord)[2:]  # Переводим код символа в двоичную систему счисления
    
    if letter_ord < 128:    # Если код символа меньше 128,
        new_data += letter  # то добавляем к новой строке оригинальный символ
    else:                                                     # Иначе
        new_letter_ord2 = letter_ord2[len(letter_ord2) - 8:]  # вычисляем последний байт кода символа в 2СС,
        new_letter_ord = int(new_letter_ord2, 2)              # переводим код символа из 2СС в 10СС,
        new_letter = chr(new_letter_ord)                      # преобразуем код символа в символ,
        new_data += new_letter                                # добавляем к новой строке полученный символ

print(new_data)  # Выводим новую строку
