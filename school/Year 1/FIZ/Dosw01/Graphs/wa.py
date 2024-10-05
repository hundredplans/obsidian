import numpy as np
import matplotlib.pyplot as plt

# Given data
a = np.array([5.5, 5.5, 5.5, 5.5, 5.5, 94.5, 89.0, 84.0, 79.0, 74.5])
b = np.array([94.5, 89.5, 84.5, 79.5, 74.5, 5.5, 6.0, 6.0, 6.0, 5.5])
delta = 0.01

# Hyperbola function
def hyperbola(a, f):
    return a * f / (a - f)

# Focal length (estimated from the data)
f = 100

# Generate a range of 'a' values for plotting
a_range = np.linspace(0, 100, 1000)

# Plot the data and hyperbola
plt.figure(figsize=(10, 10))
plt.title("Lens 1: Relationship b(a)")

# Plot the hyperbola
plt.plot(a_range, hyperbola(a_range, f), color='blue', linestyle='-', label=f'Hyperbola (f={f} cm)')

# Plot the data points
plt.errorbar(a, b, xerr=delta, yerr=delta, fmt='o', capsize=5, capthick=1, ecolor='red', label='Data points')

plt.xlabel("a (cm)")
plt.ylabel("b (cm)")
plt.legend()
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
