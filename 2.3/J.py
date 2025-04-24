# Маршрут построен

x = y = 0

while (data := input()) != 'СТОП':
    match data:
        case 'СЕВЕР':
            x += int(input())
        case 'ЮГ':
            x -= int(input())
        case 'ВОСТОК':
            y += int(input())
        case 'ЗАПАД':
            y -= int(input())

print(x, y, sep='\n')
