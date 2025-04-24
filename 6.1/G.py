# Шахматная подготовка

"""
0 = чёрная, 1 = белая
левая верхняя = 1
"""

import numpy as np


def make_board(size):
    desk = np.array([[(x + (y % 2)) % 2 for x in range(size)] for y in range(1, size + 1)], dtype="int8")
    return desk
