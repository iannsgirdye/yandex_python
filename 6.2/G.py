# Отчёт неуспеваемости

import pandas as pd


def need_to_work_better(data) -> pd.DataFrame:
    return data[(data["maths"] == 2) | (data["physics"] == 2) | (data["computer science"] == 2)]
