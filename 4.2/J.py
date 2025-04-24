# Ключевой секрет


def secret_replace(text, **replaces):
    text = list(text)
    for letter in replaces:
        count = 0
        for i in range(len(text)):
            if text[i] == letter:
                text[i] = replaces[letter][count % len(replaces[letter])]
                count += 1
    return ''.join(text)
