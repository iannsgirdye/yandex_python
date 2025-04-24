# А роза упала на лапу Азора 7.0


def is_palindrome(data):
    if type(data) is int:
        data = str(data)
    for i in range(len(data) // 2 + 1):
        if data[i] != data[len(data) - i - 1]:
            return False
    return True
