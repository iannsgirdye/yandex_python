# Властелин Чисел: Братство общей цифры

_1, _2, _3 = _1, _2, _3 = int(input()), int(input()), int(input())

if _1 % 10 == _2 % 10 == _3 % 10:
    print(_1 % 10)
elif _1 // 10 == _2 // 10 == _3 // 10:
    print(_1 // 10)
