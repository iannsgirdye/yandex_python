# Список покупок

data = [input().split(', ') for x in range(3)]
data = sorted(data[0] + data[1] + data[2])

for number in range(len(data)):
    print(str(number + 1) + '.', data[number])
