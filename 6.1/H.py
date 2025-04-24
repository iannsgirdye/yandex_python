# Числовая змейка 3.0

"""
M - ширина змеи
N - высота змеи
"H" - горизонтальная змейка
"V" - вертикальная змейка
"""

import numpy as np


def snake(M, N, direction="H"):
    if direction == "V":
        M, N = N, M
            
    result = np.array([[number + M * line for number in range(1, M + 1)] for line in range(N)], dtype="int16")

    for i in range(1, N, 2):
        for j in range(M // 2):
            result[i][j], result[i][M - 1 - j] = result[i][M - 1 - j], result[i][j]

    if direction == "V":
        result = result.transpose()
        
    return result
