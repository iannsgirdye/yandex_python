# Однофамильцы

people = [input() for x in range(int(input()))]
result = 0

for person in people:
    if people.count(person) > 1:
        result += 1

print(result)