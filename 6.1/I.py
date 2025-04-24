# Вращение

import numpy as np


def rotate(matrix, corner):
    return np.rot90(matrix, -corner // 90)
