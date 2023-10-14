import numpy as np
from matplotlib import pyplot as plt

from square import square_function, square_function_g, square_function_h
from exponential import exp_function, exp_function_g, exp_function_h


# modulation = c
# length_decrease = p
# position = initial position
def backtrack(modulation, length_decrease, init_alpha, f, position_vector, direction_vector, f_g):
    alpha = init_alpha
    while f(position_vector + alpha * direction_vector) > f(position_vector) + alpha * modulation * np.dot(
            direction_vector, f_g(position_vector)):
        alpha = length_decrease * alpha
    return alpha


def quasi_newton_dfp(c, f_g, position):
    return - c @ f_g(position)


def quasi_newton_bfgs(b, f_g, position):
    return - np.linalg.inv(b) @ f_g(position)


def update_dfp(y_k, s_k, c):
    c = c - (c @ (np.outer(y_k, y_k) @ c)) / (y_k @ c @ y_k) + np.outer(s_k, s_k) / np.dot(s_k, y_k)
    return c


def update_bfgs(y_k, s_k, b):
    b = b - (b @ (np.outer(s_k, s_k) @ b)) / (s_k @ b @ s_k) + np.outer(y_k, y_k) / np.dot(y_k, s_k)
    return b


def optimization_function(f_name, f, f_g, f_h, position, tolerance_f, tolerance_x, max_iteration=300):
    # Output x, f(x)

    modulation = 0.1
    length_decrease = 0.5
    init_alpha = 1

    iterations = 0
    initial_c = np.eye(2)
    c = initial_c
    print("\nMethod: Quasi newton ", f_name)
    while True:
        if f_name == 'DFP':
            direction = quasi_newton_dfp(c, f_g, position)
        elif f_name == 'BFGS':
            direction = quasi_newton_bfgs(c, f_g, position)
        # direction = newtons_method(f_g, f_h, position)
        alpha = backtrack(modulation=modulation, length_decrease=length_decrease, init_alpha=init_alpha, f=f,
                          position_vector=position, direction_vector=direction, f_g=f_g)
        position_copy = position.copy()
        changed_position = position + alpha * direction
        if np.linalg.norm(changed_position - position_copy) < tolerance_x or (iterations > max_iteration):
            break

        y_k = f_g(changed_position) - f_g(position_copy)
        s_k = changed_position - position_copy
        if f_name == 'DFP':
            c = update_dfp(y_k, s_k, c)
        elif f_name == 'BFGS':
            c = update_bfgs(y_k, s_k, c)
        iterations += 1
        print(iterations, changed_position, abs(f(changed_position) - f(position_copy)))
        position = changed_position
    return changed_position, f(changed_position)


optimization_function("DFP", square_function, square_function_g, square_function_h, np.array([50, 50]), 0.0001, 0.0001,
                      300)
optimization_function("DFP", exp_function, exp_function_g, exp_function_h, np.array([2, 1]), 0.0001, 0.0001, 300)

optimization_function("BFGS", square_function, square_function_g, square_function_h, np.array([50, 50]), 0.0001, 0.0001,
                      300)
optimization_function("BFGS", exp_function, exp_function_g, exp_function_h, np.array([2, 1]), 0.0001, 0.0001, 300)
