# Польский калькулятор

line = input().split()

while len(line) != 1:
    for i in range(len(line)):
        if line[i] in '-+*:/':
            line[i] = str(eval(line[i - 2] + line[i] + line[i - 1]))
            del line[i - 1], line[i - 2]
            break

print(line[0])