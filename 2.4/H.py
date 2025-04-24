# Максимальная сумма 

people = int(input())

winner = ''
max_sum_num = -(10 ** 10)
for i in range(people):
    name = input()
    num = int(input())
    
    sum_num = 0
    while num > 0:
        sum_num += num % 10
        num //= 10
        
    if sum_num >= max_sum_num:
        max_sum_num = sum_num
        winner = name

print(winner)
