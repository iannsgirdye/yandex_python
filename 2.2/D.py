# Список победителей

petya = int(input())
vasya = int(input())
tolya = int(input())

if petya > vasya and petya > tolya:
    print("1. Петя")
    if vasya > tolya:
        print("2. Вася\n3. Толя")
    else:
        print("2. Толя\n3. Вася")
elif vasya > petya and vasya > tolya:
    print("1. Вася")
    if petya > tolya:
        print("2. Петя\n3. Толя")
    else:
        print("2. Толя\n3. Петя")
else:
    print("1. Толя")
    if petya > vasya:
        print("2. Петя\n3. Вася")
    else:
        print("2. Вася\n3. Петя")
