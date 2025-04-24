# Большое число

people = int(input())

result = ''
for i in range(people):
    num = int(input())
    max_figure = -1
    
    while num > 0:
        max_figure = max(num % 10, max_figure)
        num //= 10
    
    result += str(max_figure)
    
print(result)
