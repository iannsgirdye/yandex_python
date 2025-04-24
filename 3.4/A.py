# Автоматизация списка

string = input().split()

for number, word in enumerate(string, 1):
    print(str(number) + '.', word)
