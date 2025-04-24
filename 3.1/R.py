# RLE

string = input()

count = 1
for i in range(1, len(string)):
    if (string[i] == string[i - 1]):
        count += 1
        if i == len(string) - 1:
            print(string[i], count)
    
    else:
        print(string[i - 1], count)
        count = 1
        if i == len(string) - 1:
            print(string[i], count)
