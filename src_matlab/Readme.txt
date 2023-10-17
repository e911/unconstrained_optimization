Project 2: Unconstrained Optimization
######################################
Authors: Deepak Pandita, Pujan Thapa
Date: 10/17/23
######################################

In this project, we experiment with 3 optimization functions - Gradient Descent, Newton's Method, and Quasi-Newton Method.

The files required are:
1. gradientDescent.m
2. newton.m
3. quasiNewton.m
4. backtrackingLineSearch.m
5. project2.m
6. fun1.m, fun2.m, fun3.m
7. g_fun1.m, g_fun2.m, and g_fun3.m
8. h_fun1.m, h_fun2.m, and h_fun3.m
######################################

For Gradient Descent, run:
"gradientDescent(f, g, x, eps, max_iter)"

This function expects five inputs:
1. "f" is the objective function to be optimized
2. "g" is the gradient of the objective function
3. "x" is the starting position
4. "eps" is the tolerance
5. "max_iter" is the maximum number of iterations allowed

This function returns the optimum value found, the sequence of values of the function in the optimization path,
and the sequence of values abs(f(k)-f(k-1)) in the optimization path.
######################################

For Newton's method, run:
"newton(f, g, h, x, eps, max_iter)"

This function expects six inputs:
1. "f" is the objective function to be optimized
2. "g" is the gradient of the objective function
3. "h" is the hessian of the objective function
4. "x" is the starting position
5. "eps" is the tolerance
6. "max_iter" is the maximum number of iterations allowed

This function returns the optimum value found, the sequence of values of the function in the optimization path,
and the sequence of values abs(f(k)-f(k-1)) in the optimization path.
######################################

For Quasi-Newton method, run:
"quasiNewton(f, g, h, x, eps, max_iter)"

This function expects six inputs:
1. "f" is the objective function to be optimized
2. "g" is the gradient of the objective function
3. "h" is the hessian of the objective function
4. "x" is the starting position
5. "eps" is the tolerance
6. "max_iter" is the maximum number of iterations allowed

This function returns the optimum value found, the sequence of values of the function in the optimization path,
and the sequence of values abs(f(k)-f(k-1)) in the optimization path.
######################################

"fun1.m", "fun2.m", and "fun3.m" contain the three functions given in the project description
"g_fun1.m", "g_fun2.m", and "g_fun3.m" contain the gradient of the three functions given in the project description
"h_fun1.m", "h_fun2.m", and "h_fun3.m" contain the hessian of the three functions given in the project description
######################################

"project2.m" contains the code for the experiments and plots on three objective functions given in the project description. The generated plots are saved in the working directory.
