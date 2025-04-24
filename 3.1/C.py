# Анонс новости

L = int(input())  # необходимая длина заголовка 
N = int(input())  # количество заголовкой, которое требуется сократить

for number_line in range(N):
    string = input()
    if len(string) <= L:
        print(string)
    else:
        print(string[:L - 3] + '...')
