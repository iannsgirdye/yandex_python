# Ошибка кассового аппарата

N = int(input())
M = int(input())
K1 = int(input())
K2 = int(input())

x = (M - K2) / (K1 - K2)
weight1 = int(N * x)
weight2 = int(N * (1 - x))
print(weight1, weight2)

'''
K1 * x + K2 * (1 - x) = M
K1 * x + K2 - K2 * x = M
x (K1 - K2) = M - K2
x = (M - K2) / (K1 - K2)
'''
