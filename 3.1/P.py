# Анонс новости 2.0

L = int(input())  # необходимая длина заголовка
N = int(input())  # количество строк в заголовке страницы
L -= 3

text = []
for i in range(N):
    text.append(input())

for j in range(N):
    if L - len(text[j]) > 0:
        print(text[j])
        L -= len(text[j])
    else:
        print(text[j][:L] + '...')
        break
