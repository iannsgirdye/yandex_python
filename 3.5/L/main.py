# Разделяй и властвуй

file_numbers = open(input(), 'r', encoding='UTF-8')  # Открываем файл с входными данными
data = file_numbers.read().split('\n')  # Создаём файл со строками исходного файла
file_numbers.close()  # Закрываем файл с входными данными

even, odd, eq = [], [], []  # Создаём списки для чисел под условие задачи
for line in data:
    even_line, odd_line, eq_line = [], [], []  # Создаём списки для чисел в каждой строке
    line = line.split()  # Разделяем строку по пробелам на числа
    for number in line:  # Перебираем все числа
        count0, count1 = 0, 0  # Создаём счётчики чётных и нечётных цифр числа
        for figure in number:  # Считаем количество чётных и нечётных цифр
            if figure in '02468':
                count0 += 1
            else:
                count1 += 1
        if count0 > count1:  # Добавляем число в нужный список
            even_line.append(number)
        elif count0 < count1:
            odd_line.append(number)
        else:
            eq_line.append(number)
    even.append(' '.join(even_line))  # Формируем строки для записи
    odd.append(' '.join(odd_line))
    eq.append(' '.join(eq_line))

even = '\n'.join(even)  # Формируем строки для записи результатов в файлы
odd = '\n'.join(odd)
eq = '\n'.join(eq)

file_even = open(input(), 'w', encoding='UTF-8')  # Записываем результаты в файлы
file_even.write(even)   
file_even.close()

file_odd = open(input(), 'w', encoding='UTF-8')
file_odd.write(odd)   
file_odd.close()

file_eq = open(input(), 'w', encoding='UTF-8')
file_eq.write(eq)   
file_eq.close()
