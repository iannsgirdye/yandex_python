# Польский калькулятор — 2

line = input().split()
for x in range(len(line)):
    if line[x] not in '+-*/~!#@':
        line[x] = int(line[x])

while len(line) != 1:
    for i in range(len(line)):
        
        if line[i] == '~':
            line[i - 1] *= -1
            del line[i]
            break
                
        elif line[i] == '!':
            new_line_i_minus_1 = 1
            for j in range(2, line[i - 1] + 1):
                new_line_i_minus_1 *= j
            line[i - 1] = new_line_i_minus_1
            del line[i]
            break
        
        elif line[i] == '#':
            line[i] = line[i - 1]
            break
        
        elif line[i] == '+':
            line[i] = line[i - 2] + line[i - 1]
            del line[i - 1], line[i - 2]
            break
        
        elif line[i] == '-':
            line[i] = line[i - 2] - line[i - 1]
            del line[i - 1], line[i - 2]
            break
        
        elif line[i] == '*':
            line[i] = line[i - 2] * line[i - 1]
            del line[i - 1], line[i - 2]
            break
        
        elif line[i] == '/':
            line[i] = line[i - 2] // line[i - 1]
            del line[i - 1], line[i - 2]
            break
        
        elif line[i] == '@':
            line[i - 3], line[i - 2], line[i - 1] = line[i - 2], line[i - 1], line[i - 3]
            del line[i]
            break

print(line[0])
