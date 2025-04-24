# Чётная фильтрация

print(*filter(lambda x: sum(list(map(int, list(str(x))))) % 2 == 0, (32, 64, 128, 256, 512)))