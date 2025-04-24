# Мы делили апельсин

parts = int(input())

print('А Б В')
for a in range(1, parts):
    for b in range(1, parts):
        for v in range(1, parts):
            if a + b + v == parts:
                print(a, b, v)
