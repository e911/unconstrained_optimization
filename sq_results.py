from hessian import *
from square import *


x_vector = np.array([1.0, 1.0])

first_numerical_grad_sq = first_order_grad(square_function, x_vector)
second_numerical_grad_sq = second_order_grad(square_function, x_vector)
print("Order First Gradient value:\n", first_numerical_grad_sq)
print("")
print("Order Second Gradient value:\n", second_numerical_grad_sq)
print("")
print("True Gradient value:\n", square_function_g(x_vector))
print("")

first_numerical_hessian_sq = first_order_hessian(square_function, x_vector)
second_numerical_hessian_sq = second_order_hessian(square_function, x_vector)
print("Order First Hessian value:\n", first_numerical_hessian_sq)
print("")
print("Order Second Hessian value:\n", second_numerical_hessian_sq)
print("")
print("True Hessian value:\n", square_function_h(x_vector))

