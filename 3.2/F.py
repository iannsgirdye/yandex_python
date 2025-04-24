# Кашееды — 3

people = [input() for x in range(int(input()) + int(input()))]
who_love = sorted([x for x in people if people.count(x) == 1])

if len(who_love) > 0:
    for person in who_love:
        print(person)
else:
    print('Таких нет')
