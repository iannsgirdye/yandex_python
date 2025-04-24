# Найдётся всё 3.0

import sys

find = input().lower()
flag = True

for line in sys.stdin:
    file_name = line.rstrip('\n')
    with open(file_name, 'r', encoding='UTF-8') as file:
        file_data = file.read()
        while ('  ' in file_data) or ('\t' in file_data) or ('\n' in file_data):
            if '\t' in file_data:
                file_data = file_data.replace('\t', ' ')
            if '\n' in file_data:
                file_data = file_data.replace('\n', ' ')
            if '  ' in file_data:
                file_data = file_data.replace('  ', ' ')
        if find in file_data.lower():
            print(file_name)
            flag = False
            
if flag:
    print('404. Not Found')
