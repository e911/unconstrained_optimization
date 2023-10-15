import numpy as np


def function1(x):
    return sum([(i + 1) * x[i] ** 2 for i in range(len(x))])


def function1_gradient(x):
    return 2 * np.array([(i + 1) * x[i] for i in range(len(x))])


def function1_hessian(x):
    return 2 * np.diag([(i + 1) for i in range(len(x))])


b = np.loadtxt('func2_data/fun2_b.txt')
c = np.loadtxt('func2_data/fun2_c.txt')
with open('func2_data/fun2_A.txt', 'r') as file:
    data = file.read().split()
A = np.array(data, dtype=float).reshape(500, 100)


def function2(x):
    return np.dot(c, x) - np.sum(np.nan_to_num(np.log(b - np.dot(A, x)), nan=0))

def function2_gradient(x):
    return c + np.dot(A.T, 1 / (b - np.dot(A, x)))

def function2_hessian(x):
    return np.dot(np.dot(A.T, np.diag(1 / ((b - np.dot(A, x)) ** 2))), A)
def function3(x):
    return 100 * (x[1] - x[0] ** 2) ** 2 + (1 - x[0]) ** 2


def function3_gradient(x):
    return np.array([-400 * x[0] * (x[1] - x[0] ** 2) - 2 * (1 - x[0]), 200 * (x[1] - x[0] ** 2)])


def function3_hessian(x):
    return np.array([
        [-400 * x[1] + 1200 * x[0] ** 2 + 2, -400 * x[0]],
        [-400 * x[0], 200]
    ])
