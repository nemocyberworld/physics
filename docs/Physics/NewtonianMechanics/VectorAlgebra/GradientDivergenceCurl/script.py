import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# Create a grid of points
x = y = np.linspace(-2, 2, 20)
x, y = np.meshgrid(x, y)

# Scalar field: f(x, y) = x^2 + y^2
f = x**2 + y**2

# Gradient of the scalar field
df_dx = 2 * x
df_dy = 2 * y

# Plot scalar field
fig1 = plt.figure(figsize=(10, 6))
ax1 = fig1.add_subplot(111, projection='3d')
surf = ax1.plot_surface(x, y, f, cmap=cm.viridis)
ax1.set_title('Scalar Field: f(x, y) = x² + y²')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('f(x, y)')
fig1.colorbar(surf, shrink=0.5, aspect=5)

# Plot gradient vector field
fig2, ax2 = plt.subplots(figsize=(8, 6))
strm = ax2.quiver(x, y, df_dx, df_dy, color='red')
ax2.set_title('Gradient Field: ∇f(x, y) = (2x, 2y)')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_aspect('equal')

# Vector field for divergence and curl
Fx = -y
Fy = x

# Divergence: dFx/dx + dFy/dy = 0 + 0 = 0 (uniform rotation field)
# Curl (in 2D): ∂Fy/∂x - ∂Fx/∂y = 1 - (-1) = 2

# Plot vector field
fig3, ax3 = plt.subplots(figsize=(8, 6))
ax3.quiver(x, y, Fx, Fy, color='blue')
ax3.set_title('Vector Field: F = (-y, x) — Circular Rotation (Curl ≠ 0)')
ax3.set_xlabel('x')
ax3.set_ylabel('y')
ax3.set_aspect('equal')

plt.tight_layout()
plt.show()
