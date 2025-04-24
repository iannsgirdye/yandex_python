# Территория зла

a, b, c = int(input()), int(input()), int(input())

a2, b2, c2 = a ** 2, b ** 2, c ** 2
if (a2 > b2 + c2) or (b2 > c2 + a2) or (c2 > a2 + b2):
    print('велика')
elif (a2 == b2 + c2) or (b2 == c2 + a2) or (c2 == a2 + b2):
    print('100%')
else:
    print('крайне мала')
