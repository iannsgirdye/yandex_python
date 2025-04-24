# Массовое возведение в степень 2.0

numbers = list(map(int, input().split()))
P = int(input())

for i in range(len(numbers)):
    numbers[i] = str(numbers[i] ** P)
    
print(' '.join(numbers))
