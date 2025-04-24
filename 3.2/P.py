# Зайка — 10

result = set()

while (line := input()) != '':
    line = line.split()
    for i in range(len(line)):
        if line[i] == 'зайка':
            if i == 0:
                result.add(line[i + 1])
            elif i == len(line) - 1:
                result.add(line[i - 1])
            else:
                result.add(line[i + 1])
                result.add(line[i - 1])

for element in result:
    print(element)
