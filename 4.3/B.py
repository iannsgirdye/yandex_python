# Рекурсивный сумматор цифр


def recursive_digit_sum(number):
    if number // 10 == 0:
        return number
    return recursive_digit_sum(number // 10) + (number % 10) 
