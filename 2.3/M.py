# Первому игроку приготовиться 2.0

count = int(input())

result = 'Я' * 100
for i in range(count):
    result = min(result, input())
    
print(result)
