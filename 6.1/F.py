# Матрица умножения

import numpy as np


def multiplication_matrix(N):
    table = np.array([[x * n for x in range(1, N + 1)] for n in range(1, N + 1)])
    return table
