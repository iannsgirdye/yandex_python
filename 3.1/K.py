# Найдётся всё

N = int(input())

searches = []
for i in range(N):
    searches.append(input())

key_word = input().lower()
for search in searches:
    if key_word in search.lower():
        print(search)
