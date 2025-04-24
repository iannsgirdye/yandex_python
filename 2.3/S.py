# Игра в "Угадайку"

number = 500
down = 0
up = 1000
print(number)

while (user := input()) != 'Угадал!':
    match user:
        case 'Меньше':
            up = number
        case 'Больше':
            down = number
    number = (up - down) // 2 + (up - down) % 2 + down
    print(number)
