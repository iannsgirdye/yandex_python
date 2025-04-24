# Сортировка слиянием | программа не прошла все тесты


def merge_sort(data: list) -> list:
    ready = True
    for i in range(len(data) - 1):
        if data[i] > data[i + 1]:
            data[i + 1], data[i] = data[i], data[i + 1]
            ready = False  # Внесены исправления, нужна проверка
    
    if not ready:
        result = merge_sort(data)
    
    result = data
    return result


print(merge_sort([1, 4, 2, 5, 8, 9, 0]))
