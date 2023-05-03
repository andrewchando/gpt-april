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


# More advanced limits: 


# The limit of sin(x)/x as x approaches 0: f(x) = sin(x)/x
# func = sp.sin(x)/x
# label = "y=sin(x)/x"

# The limit of (1-cos(x))/x as x approaches 0: f(x) = (1 - sp.cos(x))/x
# func = (1 - sp.cos(x))/x
# label = "y=(1-cos(x))/x"

# The limit of (e^x - 1)/x as x approaches 0: f(x) = (sp.exp(x) - 1)/x
# func = (sp.exp(x) - 1)/x
# label = "y=(e^x - 1)/x"

# The limit of ln(x+1)/x as x approaches 0: f(x) = sp.log(x+1)/x
# func = sp.log(x+1)/x
# label = "y=ln(x+1)/x"

# The limit of (sqrt(x+1) - 1)/x as x approaches 0: f(x) = (sp.sqrt(x+1) - 1)/x
func = (sp.sqrt(x+1) - 1)/x
label = "y=(sqrt(x+1) - 1)/x"

# The limit of x^x as x approaches 0: f(x) = x**x
# Note: It's generally considered that 0^0 is an undetermined form. However, the limit of x^x as x approaches 0 is 1.
# func = x**x
# label = "y=x^x"

# The limit of (x^3 - 8)/(x - 2) as x approaches 2: f(x) = (x**3 - 8)/(x - 2)
# func = (x**3 - 8)/(x - 2)
# label = "y=(x^3 - 8)/(x - 2)"

# The limit of (x^4 - 16)/(x - 2) as x approaches 2: f(x) = (x**4 - 16)/(x - 2)
# func = (x**4 - 16)/(x - 2)
# label = "y=(x^4 - 16)/(x - 2)"


# Calculate the limit and plot the function
print("The limit of the function as x approaches 0: ", calculate_limit(func, x, 0))
plot_func(func, label)
