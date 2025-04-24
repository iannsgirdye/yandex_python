# Без комментариев 2.0

from sys import stdin

for line in stdin:
    if '#' in line:
        if '#' == line[0]:
            continue
        else:
            print(line.rstrip()[:line.index('#')])
    else:
        print(line.rstrip())
