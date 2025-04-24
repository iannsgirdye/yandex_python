# Математическая выгода

n = int(input())

max_sum_figures = -1
base = -1
for i in range(2, 10 + 1):
    num = n
    sum_figures = 0
    while num > 0:
        sum_figures += num % i
        num //= i
    
    if sum_figures > max_sum_figures:
        max_sum_figures = sum_figures
        base = i
        
print(base)
