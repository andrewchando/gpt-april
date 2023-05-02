import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

# Define the variable
x = sp.symbols('x')

# Define a function for limit
def calculate_limit(func, variable, point):
    return sp.limit(func, variable, point)

# Define a function for plotting
def plot_func(func, label):
    func_lambdified = sp.lambdify(x, func, "numpy")
    X_vals = np.linspace(-10, 10, 400)
    Y_vals = func_lambdified(X_vals)
    plt.plot(X_vals, Y_vals, label=label)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

# Define the function you want to work with
# Uncomment the function and label you want to test

# The limit of a constant is the constant itself: f(x) = 5
# func = 5
# label = "y=5"

# The limit of x as x approaches a is a: f(x) = x
# func = x
# label = "y=x"

# The limit of a function at a point where the function is defined: f(x) = x^2
# func = x**2
# label = "y=x^2"

# The limit of a sum: f(x) = x^2 + x^3
# func = x**2 + x**3
# label = "y=x^2 + x^3"

# The limit of a product: f(x) = x^2 * x^3
# func = x**2 * x**3
# label = "y=x^2 * x^3"

# The limit of a quotient: f(x) = x^2 / x^3 (excluding x=0)
# func = x**2 / x**3
# label = "y=x^2 / x^3"




# Calculate the limit and plot the function
print("The limit of the function as x approaches 0: ", calculate_limit(func, x, 0))
plot_func(func, label)
