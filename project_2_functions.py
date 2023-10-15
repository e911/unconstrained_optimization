import numpy as np


def function1(x):
    return sum([(i + 1) * x[i] ** 2 for i in range(len(x))])


def function1_gradient(x):
    return 2 * np.array([(i + 1) * x[i] for i in range(len(x))])


def function1_hessian(x):
    return 2 * np.diag([(i + 1) for i in range(len(x))])


A = np.loadtxt('func2_data/fun2_A.txt')
b = np.loadtxt('func2_data/fun2_A.txt')
c = np.loadtxt('func2_data/fun2_A.txt')


def function2(x):
    return c.T.dot(x) - np.sum(np.log(b - A.dot(x)))


def function2_gradient(x):
    return c + A.T.dot(1 / (b - A.dot(x)))


def function2_hessian(x):
    return A.T.dot(np.diag(1 / ((b - A.dot(x)) ** 2))).dot(A)


def function3(x):
    return 100 * (x[1] - x[0] ** 2) ** 2 + (1 - x[0]) ** 2


def function3_gradient(x):
    return np.array([-400 * x[0] * (x[1] - x[0] ** 2) - 2 * (1 - x[0]), 200 * (x[1] - x[0] ** 2)])


def function3_hessian(x):
    return np.array([
        [-400 * x[1] + 1200 * x[0] ** 2 + 2, -400 * x[0]],
        [-400 * x[0], 200]
    ])
