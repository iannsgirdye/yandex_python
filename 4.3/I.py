# Циклический генератор

def cycle(numbers):
    while True:
        for number in numbers:
            yield number
