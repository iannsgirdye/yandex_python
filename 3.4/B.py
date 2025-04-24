# Сборы на прогулку

kids_1 = input().split(', ')
kids_2 = input().split(', ')

for pair in list(zip(kids_1, kids_2)):
    print(pair[0], '-', pair[1])
