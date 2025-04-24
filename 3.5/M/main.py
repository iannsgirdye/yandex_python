# Обновление данных

from json import dump, load
from sys import stdin

name_file = input()
file = open(name_file, 'r', encoding='UTF-8')
data = load(file)
file.close()

for line in stdin:
    line = line.split()
    data[line[0]] = line[2]

file = open(name_file, 'w', encoding='UTF-8')
dump(data, file, ensure_ascii=False, indent=4)
file.close()
