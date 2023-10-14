from exponential import *
from hessian import *


x_vector = np.array([1.0, 1.0])

first_numerical_grad_exp = first_order_grad(exp_function, x_vector)
second_numerical_grad_exp = second_order_grad(exp_function, x_vector)
print("Order First Gradient value:\n", first_numerical_grad_exp)
print("")
print("Order Second Gradient value:\n", second_numerical_grad_exp)
print("")
print("True Gradient value:\n", exp_function_g(x_vector))
print("")

first_numerical_hessian_exp = first_order_hessian(exp_function, x_vector)
second_numerical_hessian_exp = second_order_hessian(exp_function, x_vector)
print("Order First Hessian value:\n", first_numerical_hessian_exp)
print("")
print("Order Second Hessian value:\n", second_numerical_hessian_exp)
print("")
print("True Hessian value:\n", exp_function_h(x_vector))
print("")
