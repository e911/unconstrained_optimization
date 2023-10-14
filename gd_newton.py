import numpy as np
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


def gradient_descent(f_g, position):
    return -1 * f_g(position)


def newtons_method(f_g, f_h, position):
    return -np.linalg.inv(f_h(position)) @ f_g(position)

def optimization_function(f_name, f, f_g, f_h, position, tolerance_f, tolerance_x, max_iteration=300):
    # Output x, f(x)

    modulation = 0.1
    length_decrease = 0.5
    init_alpha = 1

    iterations = 0
    print("\nMethod: ", f_name)
    while True:
        if (f_name == "GD"):
            direction = gradient_descent(f_g, position)
        elif(f_name == "Newton"):
            direction = newtons_method(f_g, f_h, position)
        alpha = backtrack(modulation=modulation, length_decrease=length_decrease, init_alpha=init_alpha, f=f,
                          position_vector=position, direction_vector=direction, f_g=f_g)
        position_copy = position.copy()
        changed_position = position + alpha * direction
        if np.linalg.norm(changed_position - position_copy) < tolerance_x or (iterations > max_iteration):
            break
        iterations += 1
        print(iterations, changed_position, abs(f(changed_position)-f(position)))
        position = changed_position
    return changed_position, f(changed_position)


optimization_function("GD",square_function, square_function_g, square_function_h, np.array([50, 50]), 0.0001, 0.0001, 300)
optimization_function("GD",exp_function, exp_function_g, exp_function_h, np.array([2, 1]), 0.0001, 0.0001, 300)
optimization_function("Newton",square_function, square_function_g, square_function_h, np.array([50, 50]), 0.0001, 0.0001, 300)
optimization_function("Newton",exp_function, exp_function_g, exp_function_h, np.array([2, 1]), 0.0001, 0.0001, 300)
