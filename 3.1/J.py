# Частотный анализ на минималках

string = ''
while (line := input()) != 'ФИНИШ':
    string += ''.join(line.split()).lower()

max_count_letter = float('-inf')
max_letter = ''
for letter in string:
    count_letter = string.count(letter)
    if count_letter > max_count_letter:
        max_count_letter = count_letter
        max_letter = letter
    elif (count_letter == max_count_letter) and (letter < max_letter):
        max_count_letter = count_letter
        max_letter = letter

print(max_letter)
