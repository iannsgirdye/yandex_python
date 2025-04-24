# Колода карт

from itertools import product

first = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
second = ['пик', 'треф', 'бубен', 'червей']
data = input()

for element in product(first, second):
    string = ' '.join(element)
    if data not in string:
        print(string)
