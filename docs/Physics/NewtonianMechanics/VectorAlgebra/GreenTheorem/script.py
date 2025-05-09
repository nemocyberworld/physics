import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from sympy import symbols, diff, lambdify, integrate, sin, cos, pi

# Define vector field F = (P, Q)
x, y = symbols('x y')
P = x**2 - y**2
Q = 2*x*y

# Compute the curl (partial Q/partial x - partial P/partial y)
curl = diff(Q, x) - diff(P, y)
print("Symbolic curl of F:", curl)

# Convert to numerical functions
curl_func = lambdify((x, y), curl, 'numpy')
P_func = lambdify((x, y), P, 'numpy')
Q_func = lambdify((x, y), Q, 'numpy')

# Define region (unit circle)
theta = np.linspace(0, 2 * np.pi, 300)
x_circ = np.cos(theta)
y_circ = np.sin(theta)

# Plot vector field and region
X, Y = np.meshgrid(np.linspace(-1.2, 1.2, 20), np.linspace(-1.2, 1.2, 20))
U = P_func(X, Y)
V = Q_func(X, Y)

plt.figure(figsize=(8, 8))
plt.quiver(X, Y, U, V, color='darkgreen', alpha=0.6)
plt.plot(x_circ, y_circ, 'b-', label='Curve C (unit circle)')
plt.fill(x_circ, y_circ, color='lightblue', alpha=0.3)
plt.title("Vector Field F and Curve C")
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.show()

# Evaluate double integral over disk using polar coordinates
r, t = symbols('r t')
polar_expr = 4 * r * sin(t) * r
area_integral = integrate(integrate(polar_expr, (t, 0, 2*pi)), (r, 0, 1))
print("Value of the double integral (Green's Theorem):", area_integral)

# Helpful message
print("\nThis script visualizes Green's Theorem by showing a vector field over the unit disk.\n")