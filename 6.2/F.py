# Отчёт успеваемости

import pandas as pd


def best(data) -> pd.DataFrame:
    return data[(data["maths"] > 3) & (data["physics"] > 3) & (data["computer science"] > 3)]
