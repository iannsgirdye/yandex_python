# Сколько вешать в байтах?

import os
import math

size = os.stat(input()).st_size

if size >= 2 ** 30:
    size = size / 2 ** 30
    name_size = 'ГБ'
elif size >= 2 ** 20:
    size = size / 2 ** 20
    name_size = 'МБ'
elif size >= 2 ** 10:
    size = size / 2 ** 10
    name_size = 'КБ'
else:
    name_size = 'Б'

print(math.ceil(size), name_size, sep='')
