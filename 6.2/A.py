# Длины всех слов - 2

import pandas as pd


def length_stats(text) -> pd.Series:
    # Удаление пунктуационных знаков из текста и его разделение по пробелам
    words = "".join(symbol for symbol in text.lower() if symbol.isalpha() or symbol == " ").split()
    words = sorted(list(set(words)))  # Удаление повторяющихся слов и сортировка оставшихся
    
    return pd.Series([len(word) for word in words], index=words)
