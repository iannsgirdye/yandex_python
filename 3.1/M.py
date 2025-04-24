# Массовое возведение в степень

N = int(input())  # количество чисел

numbers = []  # числа
for i in range(N):
    numbers.append(int(input()))
    
P = int(input())  # степень
for j in range(N):
    print(numbers[j] ** P)
