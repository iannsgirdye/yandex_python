# Длинные слова

import pandas as pd


def get_long(data, min_length=5) -> pd.Series:
    return data[data >= min_length]
