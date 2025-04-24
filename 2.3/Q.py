# Чётная чистота

n = input()

result = ''
for i in n:
    if int(i) % 2 == 1:
        result += i

print(result)
