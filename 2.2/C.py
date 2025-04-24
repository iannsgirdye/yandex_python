# Кто быстрее на этот раз?

petya = int(input())
vasya = int(input())
tolya = int(input())

if petya > vasya and petya > tolya:
    print("Петя")
elif vasya > petya and vasya > tolya:
    print("Вася")
else:
    print("Толя")
    