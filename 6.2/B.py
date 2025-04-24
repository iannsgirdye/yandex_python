# Длины всех слов по чётности

import pandas as pd


def length_stats(text) -> tuple:
    # Удаление пунктуационных знаков из текста и его разделение по пробелам
    words = "".join(symbol for symbol in text.lower() if symbol.isalpha() or symbol == " ").split()
    words = sorted(list(set(words)))  # Удаление повторяющихся слов и сортировка оставшихся
    
    odd_words = [word for word in words if len(word) % 2 == 1]    # слова с нечётным количеством букв
    even_words = [word for word in words if len(word) % 2 == 0]  # слова с чётным количеством букв
    
    odd_result = pd.Series([len(word) for word in odd_words], index=odd_words, dtype="int64")
    even_result = pd.Series([len(word) for word in even_words], index=even_words, dtype="int64")
    
    return odd_result, even_result
