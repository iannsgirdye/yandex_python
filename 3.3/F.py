# Буквенная статистика

# n = name
# c = count_of_name
# w = letter

text = input()

result = {n: c for n, c in {(w, ''.join(text.lower().split()).count(w)) for w in ''.join(text.lower().split()) if w.isalpha()}}

print(result)

