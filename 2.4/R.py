# Новогоднее настроение 2.0

number = int(input())
n = number
count_elements = 0

while n > 0:
    count_elements += 1
    n -= count_elements

len_last_line = count_elements - 1 + n
for x in range(number - count_elements - n + 1, number + 1):
    len_last_line += len(str(x))

count_now = 0
num_line = 1
line = ''
for j in range(1, number + 1):
    line += str(j)
    count_now += 1
    
    if (count_now < num_line) and (j < number):
        line += ' '
    else:
        count_spaces = len_last_line - len(line)
        spaces_after = ' ' * ((count_spaces // 2) + (count_spaces % 2))
        spaces_before = ' ' * (count_spaces - len(spaces_after))
        print(spaces_before + line + spaces_after)
        
        count_now = 0
        num_line += 1
        line = ''
