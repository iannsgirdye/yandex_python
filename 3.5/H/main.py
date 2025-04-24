# Файловая разница

from itertools import chain

first_file = open(input(), 'r', encoding='UTF-8')
data_of_first_file = [line1.rstrip('\n').split() for line1 in first_file]
first_file.close()
data_of_first_file = set(chain.from_iterable(data_of_first_file))

second_file = open(input(), 'r', encoding='UTF-8')
data_of_second_file = [line2.rstrip('\n').split() for line2 in second_file]
second_file.close()
data_of_second_file = set(chain.from_iterable(data_of_second_file))

answer_file = open(input(), 'w', encoding='UTF-8')
data_of_answer_file = sorted(list(data_of_first_file.symmetric_difference(data_of_second_file)))
for element in data_of_answer_file:
    answer_file.writelines(element + '\n')
answer_file.close()
