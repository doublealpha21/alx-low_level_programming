from scipy.optimize import linprog

# Coefficients of the objective function
c = [-2, -3]

# Coefficients of the inequality constraints
A = [[2, 1], [2, 3]]

# Right-hand side values of the inequality constraints
b = [140, 180]

# Bounds for the decision variables x and y
x_bounds = (0, None)
y_bounds = (0, None)

# Solve the optimization problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

# Display the results
if result.success:
    x_optimal = result.x[0]
    y_optimal = result.x[1]
    max_value = -result.fun

    print("Optimal solution:")
    print("x =", x_optimal)
    print("y =", y_optimal)
    print("Maximum value of f(x, y) =", max_value)
else:
    print("Optimization failed. Check constraints or try a different method.")
