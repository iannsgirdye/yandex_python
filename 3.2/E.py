# Кашееды — 2

people = [input() for x in range(int(input()) + int(input()))]

total = 0
for person in people:
    if people.count(person) == 1:
        total += 1

if total > 0:
    print(total)
else:
    print('Таких нет')