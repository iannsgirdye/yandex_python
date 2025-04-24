# Зайка — 2

line1 = input()
line2 = input()
line3 = input()

z1 = z2 = z3 = False
word = 'зайка'

if word in line1:
    z1 = True
if word in line2:
    z2 = True
if word in line3:
    z3 = True
    
if z1 and z2 and z3:
    MIN = min(line1, line2, line3)
    print(MIN, len(MIN))
elif z1 and z2:
    MIN = min(line1, line2)
    print(MIN, len(MIN))
elif z1 and z3:
    MIN = min(line1, line3)
    print(MIN, len(MIN))
elif z2 and z3:
    MIN = min(line2, line3)
    print(MIN, len(MIN))
elif z1:
    print(line1, len(line1))
elif z2:
    print(line2, len(line2))
elif z3:
    print(line3, len(line3))
