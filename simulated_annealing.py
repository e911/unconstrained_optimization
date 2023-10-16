import matplotlib.pyplot as plt
from project_2_functions import *

def simulated_annealing(title, f, initial_position):
    initial_temperature = 300
    cooling_rate = 0.3
    num_iterations = 1500

    current_position = initial_position
    current_value = f(current_position)

    state = current_position
    cost = current_value

    changes_position_values = [current_position]
    iteration = 0
    while True:
        current_position_old = current_position.copy()
        changed_position = current_position + np.random.uniform(-0.1, 0.1, size=initial_position.shape)
        changed_value = f(changed_position)

        if acceptance_probability(current_value, changed_value, initial_temperature) > np.random.rand():
            current_position = changed_position
            current_value = changed_value
        if(abs(f(changed_position)-f(current_position_old)) < 0.0001) or iteration == num_iterations:
            break;
        initial_temperature *= 1 - cooling_rate
        iteration += 1
        changes_position_values.append(current_position)

    plt.figure(figsize=(8, 8))
    plt.plot([f(x) for x in changes_position_values])
    plt.title(title)
    plt.xlabel('Iterations')
    plt.ylabel('Change in function')
    plt.show()

    return state, cost


def acceptance_probability(old_value, changed_value, temperature):
    if changed_value < old_value:
        return 1.0
    return np.exp((old_value - changed_value) / temperature)



initial_position = np.full(100, 2)
position, value = simulated_annealing("Func1", function1, initial_position)
print("Best position found for func 1:", position)
print("Best value found for func 1:", value)

initial_position = np.full(100, 14)
position, value = simulated_annealing("Func2", function2, initial_position)
print("Best position found for func 2:", position)
print("Best value found for func 2:", value)

initial_position = np.array([1, 3])
position, value = simulated_annealing("Func3", function3, initial_position)
print("Best position found for func 3:", position)
print("Best value found for func 3:", value)

