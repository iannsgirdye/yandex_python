# В эфире рубрика «Эксперименты»

first = []
second = []


def enter_results(*numbers):
    global first, second
    for i in range(len(numbers)):
        if i % 2 == 0:
            first.append(numbers[i])
        else:
            second.append(numbers[i])
    

def get_sum():
    return round(sum(first), 2), round(sum(second), 2)


def get_average():
    return round(sum(first) / len(first), 2), round(sum(second) / len(second), 2)
