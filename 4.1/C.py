# Длина числа


def number_length(number):
    number = str(number)
    if '-' in number:
        number = number.replace('-', '')
    return len(number)
