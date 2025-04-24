# Интересное сложение

children, food = int(input()), int(input())
for_everyone = food // children
for_no_one = food % children
print(for_everyone, for_no_one, sep="\n")
