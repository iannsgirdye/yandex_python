# Кашееды

N, M = int(input()), int(input())  # манная, овсяная
love_N, love_M = {input() for n in range(N)}, {input() for m in range(M)}

total = len(love_N & love_M)
if total > 0:
    print(total)
else:
    print('Таких нет')