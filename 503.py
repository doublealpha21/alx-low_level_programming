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
