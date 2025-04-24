# Друзья друзей

first_level = dict()
second_level = dict()
people = []

while (line := input()) != '':
    line = line.split()
    first_level[line[0]] = first_level.get(line[0], []) + [line[1]]
    first_level[line[1]] = first_level.get(line[1], []) + [line[0]]
    first_level[line[0]].sort()
    first_level[line[1]].sort()
    people.append(line[0])
    people.append(line[1])
    second_level[line[0]] = []
    second_level[line[1]] = []
    
    
first_level = dict(sorted(first_level.items()))
second_level = dict(sorted(second_level.items()))
people = sorted(list(set(people)))

number = -1
for person, friends_person in first_level.items():  # проходимся по каждому человеку и списку его друзей
    number += 1
    for friend_person in friends_person:  # проходимся по каждому другу взятого человека
        for friend_friend_person in first_level.get(friend_person):  # проходимся по друзьям друга взятого человека
            if (friend_friend_person not in friends_person):
                if (friend_friend_person not in people[number]):
                    if (friend_friend_person not in second_level[person]): 
                        second_level[person].append(friend_friend_person)
                        second_level[person].sort()
            
for key, values in second_level.items():
    print(key, ':', sep='', end=' ')
    first_value = True
    for value in values:
        if first_value:
            print(value, end='')
            first_value = False
        else:
            print(',', value, end='')
    print()
