# Хвост

F = input()  # имя файла
N = int(input())  # количество строк, которые нужно вывести

file = open(F, 'r', encoding='UTF-8')
data = file.readlines()
file.close()

print(*data[len(data) - N:], sep='')
