# Лучшая защита — шифрование

number = int(input())

a = number // 100
b = (number // 10) % 10
c = number % 10

step1 = b + c
step2 = a + b

if step1 >= step2:
    step3 = str(step1) + str(step2)
else:
    step3 = str(step2) + str(step1)
    
print(step3)
