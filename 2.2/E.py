# Яблоки

petya = 7
vasya = 6
N = int(input())
M = int(input())

petya_new = petya - 3 + 2 + N
vasya_new = vasya + 3 + 5 - 2 + M

if petya_new > vasya_new:
    print("Петя")
else:
    print("Вася")
