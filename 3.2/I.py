# Зайка — 9

data = dict()

while (line := input()) != '':
    line = line.split()
    for element in line:
        data[element] = data.get(element, 0) + 1

for key, value in data.items():
    print(key, value)
