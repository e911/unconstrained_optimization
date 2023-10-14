import math

import numpy as np


def square_function(x):
    return x[0] ** 2 + 10 * x[1] ** 2


def square_function_g(x):
    return np.array([2 * x[0], 20 * x[1]])


def square_function_h(x):
    return np.array([[2, 0], [0, 20]])
