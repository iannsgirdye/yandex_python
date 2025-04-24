# Обновление журнала

import pandas as pd


def update(data: pd.DataFrame) -> pd.DataFrame:
    new_data = data.assign(average=lambda x: (x["maths"] + x["physics"] + x["computer science"]) / 3)
    return new_data.sort_values(["average", "name"], ascending=[False, True])
