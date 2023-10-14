import numpy as np


def first_order_grad(f, x, h=0.001):
    n = len(x)
    gradient = np.zeros(n)
    f_x = f(x)

    for i in range(n):
        x_h = x.copy()
        x_h[i] += h

        gradient[i] = (f(x_h) - f_x) / h

    return gradient


def second_order_grad(f, x, h=0.001):
    n = len(x)
    gradient = np.zeros(n)

    for i in range(n):
        x_h = x.copy()
        x__h = x.copy()
        x_h[i] += h
        x__h[i] -= h

        gradient[i] = (f(x_h) - f(x__h)) / (2 * h)

    return gradient
