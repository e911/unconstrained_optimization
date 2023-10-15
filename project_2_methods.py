import numpy as np
from matplotlib import pyplot as plt
from project_2_functions import *


# modulation = c
# length_decrease = p
# position = initial position
def backtrack(modulation, length_decrease, init_alpha, f, position_vector, direction_vector, f_g):
    alpha = init_alpha
    while f(position_vector + alpha * direction_vector) > f(position_vector) + alpha * modulation * np.dot(
            direction_vector, f_g(position_vector)):
        alpha = length_decrease * alpha
    return alpha


def gradient_descent(f_g, position):
    return -1 * f_g(position)


def newtons_method(f_g, f_h, position):
    return -np.linalg.inv(f_h(position)) @ f_g(position)


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
    if f_name == 'DFP' or f_name == 'BFGS':
        initial_c = np.eye(len(initial_position))
        c = initial_c
    print("\nMethod:", f_name)
    while True:
        if (f_name == "Gradient Descent"):
            direction = gradient_descent(f_g, position)
        elif(f_name == "Newton"):
            direction = newtons_method(f_g, f_h, position)
        elif f_name == 'DFP':
            direction = quasi_newton_dfp(c, f_g, position)
        elif f_name == 'BFGS':
            direction = quasi_newton_bfgs(c, f_g, position)

        # direction = newtons_method(f_g, f_h, position)
        alpha = backtrack(modulation=modulation, length_decrease=length_decrease, init_alpha=init_alpha, f=f,
                          position_vector=position, direction_vector=direction, f_g=f_g)
        position_copy = position.copy()
        changed_position = position + alpha * direction
        if np.linalg.norm(changed_position - position_copy) < tolerance_x or (iterations > max_iteration) or abs(f(changed_position) - f(position_copy)) < tolerance_f:
            break
        if f_name == 'DFP' or f_name == 'BFGS':
            y_k = f_g(changed_position) - f_g(position_copy)
            s_k = changed_position - position_copy
            if f_name == 'DFP':
                c = update_dfp(y_k, s_k, c)
            elif f_name == 'BFGS':
                c = update_bfgs(y_k, s_k, c)
        iterations += 1
        print(iterations, changed_position, abs(f(changed_position) - f(position_copy)), np.linalg.norm(changed_position - position_copy))
        position = changed_position
    return changed_position, f(changed_position)


initial_position = np.full(100, 50)
optimization_function("Gradient Descent",function1, function1_gradient, function1_hessian, initial_position, 0.0001, 0.0001, 300)
optimization_function("Newton",function1, function1_gradient, function1_hessian, initial_position, 0.0001, 0.0001, 300)
optimization_function("BFGS",function1, function1_gradient, function1_hessian, initial_position, 0.0001, 0.0001, 300)


initial_position = np.array([10, 10])
optimization_function("Gradient Descent",function3, function3_gradient, function3_hessian, initial_position, 0.0001, 0.0001, 300)
optimization_function("Newton",function3, function3_gradient, function3_hessian, initial_position, 0.0001, 0.0001, 300)
optimization_function("BFGS",function3, function3_gradient, function3_hessian, initial_position, 0.0001, 0.0001, 300)


# optimization_function("Gradient Descent",function2, function2_gradient, function2_hessian, initial_position, 0.0001, 0.0001, 300)
# optimization_function("Newton",function2, function2_gradient, function2_hessian, initial_position, 0.0001, 0.0001, 300)
# optimization_function("BFGS",function2, function2_gradient, function2_hessian, initial_position, 0.0001, 0.0001, 300)
