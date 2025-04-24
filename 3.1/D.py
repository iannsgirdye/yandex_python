# Очистка данных

while (string := input()) != '':
    if string[-3:] == '@@@':
        continue
    elif string[:2] == '##':
        print(string[2:])
    else:
        print(string)
