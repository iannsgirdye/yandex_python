# RLE наоборот

rle = [('a', 2), ('b', 3), ('c', 1)]

result = ''.join([x[0] * x[1] for x in rle])
print(result)