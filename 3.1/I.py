# Без комментариев

while (line := input()) != '':
    if '#' not in line:
        print(line)
    else:
        if '#' in line[0]:
            continue
        else:
            print(line[:line.index('#')])
