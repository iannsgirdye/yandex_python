# Автоматизация игры

num1, num2 = int(input()), int(input())

a1 = num1 // 100
b1 = (num1 // 10) % 10
c1 = num1 % 10

a2 = num2 // 100
b2 = (num2 // 10) % 10
c2 = num2 % 10

a3 = (a1 + a2) % 10
b3 = (b1 + b2) % 10
c3 = (c1 + c2) % 10

num3 = a3 * 100 + b3 * 10 + c3
print(num3)
