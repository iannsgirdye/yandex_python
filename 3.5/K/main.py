# Файловая статистика 2.0

from itertools import chain
from json import dump

file_in = open(input(), 'r', encoding='UTF-8')
data_in = list(map(int, file_in.read().split()))
file_in.close()

data_out = dict()
data_out["count"] = len(data_in)
data_out["positive_count"] = len([x for x in data_in if x > 0])
data_out["min"] = min(data_in)
data_out["max"] = max(data_in)
data_out["sum"] = sum(data_in)
data_out["average"] = round(sum(data_in) / len(data_in), 2)

file_out = open(input(), 'w', encoding='UTF-8')
dump(data_out, file_out, ensure_ascii=True, indent=4)
file_out.close()
