# На старт! Внимание! Марш!

people = int(input())

for i in range(people):
    for j in range(3 + i, 0, -1):
        print(f'До старта {j} секунд(ы)')
    print(f'Старт {i + 1}!!!')
