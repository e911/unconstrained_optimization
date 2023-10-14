import numpy as np
from gradient import first_order_grad, second_order_grad

h = 0.001


def first_order_hessian(f, x):
    n = len(x)
    hessian = np.zeros([len(x), len(x)])

    for i in range(n):
        x_h = x.copy()
        x_h[i] += h
        g1 = second_order_grad(f, x_h)
        g2 = second_order_grad(f, x)
        hessian[i] = (g1 - g2) / h
    return hessian


def second_order_hessian(f, x):
    n = len(x)
    hessian = np.zeros([len(x), len(x)])

    for i in range(n):
        x_h = x.copy()
        x_h[i] += h
        x__h = x.copy()
        x__h[i] -= h
        g1 = second_order_grad(f, x_h)
        g2 = second_order_grad(f, x__h)
        hessian[i] = (g1 - g2) / (2 * h)
    return hessian
