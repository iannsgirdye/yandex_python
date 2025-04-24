# Найдётся всё 2.0

from sys import stdin

data_original = [line.rstrip() for line in stdin]
word = data_original.pop().lower()
data = [element.lower() for element in data_original]

for i in range(len(data)):
    if word in data[i]:
        print(data_original[i])
