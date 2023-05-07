# Exploring non convex functions w matplotlib 5/7

# Explanation of the core blocks:

# Import necessary libraries: This block imports the necessary libraries for creating a 3D plot, such as numpy, matplotlib, and mpl_toolkits.

# Define the nonconvex function: This block defines the nonconvex function that you want to plot. In this case, it's a simple example, but you can replace it with any other function you want to visualize.

# Create a meshgrid for x and y axes: This block creates a meshgrid for the x and y axes using numpy's linspace and meshgrid functions.

# Calculate the z values for the nonconvex function: This block calculates the z values for each point on the meshgrid using the nonconvex function defined earlier.

# Create a 3D plot and plot the nonconvex function's surface: This block initializes a 3D plot using matplotlib and then plots the surface of the nonconvex function using the colormap coolwarm, which results in a visually appealing plot.

# Customize the z axis: This block sets the tick labels for the z axis, making it more readable.

# Add a color bar: This block adds a color bar to the plot, which helps in understanding the relationship between the colors and the z values.

# Plot the level sets: This block plots the level sets (contour lines) on the 3D plot, giving more information about the function's behavior in relation to the x and y axes.

# Add labels and title: This block adds labels for the x, y, and z


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

# Define the nonconvex function
def nonconvex_function(x, y):
    return (x**2 + y**2) * np.sin((x**2 + y**2))

# Create a meshgrid for the x and y axis
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
x, y = np.meshgrid(x, y)

# Calculate the z values for the nonconvex function
z = nonconvex_function(x, y)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


# Plot the nonconvex function's surface
surf = ax.plot_surface(x, y, z, cmap=cm.coolwarm, linewidth=0, antialiased=True, alpha=0.8)

# Customize the z axis
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors
fig.colorbar(surf, shrink=0.5, aspect=5)

# Plot the level sets (contour lines)
contour_levels = np.linspace(-10, 10, 21)
ax.contour(x, y, z, contour_levels, cmap=cm.coolwarm, linewidths=1)

# Add labels for the axes
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Set the title of the plot
ax.set_title('3D Nonconvex Function and Level Sets')

# Show the plot
plt.show()
