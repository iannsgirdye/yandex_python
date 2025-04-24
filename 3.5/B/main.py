# Средний рост

from sys import stdin

difference = []

for line in stdin:
    before = int(line.rstrip().split()[1]) 
    after = int(line.rstrip().split()[2])
    difference.append(after - before)

result = round(sum(difference) / len(difference))
print(result)
