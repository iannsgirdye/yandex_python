# Сильная цифра
 
n = int(input())

result = -1
while n != 0:
    result = max(result, n % 10)
    n //= 10
    
print(result)
