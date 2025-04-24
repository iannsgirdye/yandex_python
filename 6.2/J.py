# Экстремум функции

import numpy as np
import pandas as pd


def values(func, start: float, end: float, step: float) -> pd.Series:
    arguments = np.arange(start, end + step, step)                   # x
    data = pd.Series([func(x) for x in arguments], index=arguments)  # x и f(x)
    return data
    

def min_extremum(data: pd.Series) -> float:
    new_data = data.sort_values()
    return new_data.index[0]
    
    
def max_extremum(data: pd.Series) -> float:
    new_data = data.sort_values(ascending=False)
    return new_data.index[0]
