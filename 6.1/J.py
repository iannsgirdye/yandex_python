# Лесенка

import numpy as np


def stairs(vector):
    size = len(vector)
    result = np.array([[vector[i - j] for i in range(size)] for j in range(size)])
    return result
    