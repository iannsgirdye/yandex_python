# Шахматный «обед»


def can_eat(horse, other):
    return 5 == abs(other[1] - horse[1]) ** 2 + abs(other[0] - horse[0]) ** 2