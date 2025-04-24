# Это будет наш секрет

import string

sdvig = int(input()) % 26

with open('public.txt', 'r', encoding='UTF-8') as file_public:
    file_public_data = file_public.read()

new_data = ''
for letter in file_public_data:
    if letter.isalpha():
        letter_ord = ord(letter)
        if letter.isupper():
            if 65 <= letter_ord + sdvig <= 90:
                new_data += chr(letter_ord + sdvig)
            else:
                if sdvig > 0:
                    new_data += chr(letter_ord + sdvig - 26)
                else:
                    new_data += chr(letter_ord + sdvig + 26)
        else:
            if 97 <= letter_ord + sdvig <= 122:
                new_data += chr(letter_ord + sdvig)
            else:
                if sdvig > 0:
                    new_data += chr(letter_ord + sdvig - 26)
                else:
                    new_data += chr(letter_ord + sdvig + 26)
    else:
        new_data += letter

with open('private.txt', 'w', encoding='UTF-8') as file_private:
    file_private.write(new_data)
