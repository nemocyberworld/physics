import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a 3D grid of points
x, y, z = np.meshgrid(np.linspace(-1, 1, 10),
                      np.linspace(-1, 1, 10),
                      np.linspace(-1, 1, 10))

# Define vector field F = r = xi + yj + zk
u = x
v = y
w = z

# Compute divergence: div(F) = ∂Fx/∂x + ∂Fy/∂y + ∂Fz/∂z
# For F = xi + yj + zk, divergence = 3 everywhere
divergence = 3 * np.ones_like(x)

# Compute magnitude of vectors for coloring
magnitude = np.sqrt(u**2 + v**2 + w**2)

# Set up 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Normalize color mapping based on vector magnitude
norm_magnitude = (magnitude - magnitude.min()) / (magnitude.max() - magnitude.min())
colors = plt.cm.plasma(norm_magnitude.flatten())

# Plot vector field using quivers
ax.quiver(x, y, z, u, v, w, length=0.1, normalize=True, color=colors)

# Define cube corners for boundary visualization
r = [-1, 1]
points = np.array([[x, y, z] for x in r for y in r for z in r])

# Define edges by connecting appropriate corner indices
edges = [
    [0,1], [0,2], [0,4], [1,3], [1,5],
    [2,3], [2,6], [3,7], [4,5], [4,6],
    [5,7], [6,7]
]

# Draw cube edges
for edge in edges:
    p1, p2 = points[edge[0]], points[edge[1]]
    ax.plot([p1[0], p2[0]],
            [p1[1], p2[1]],
            [p1[2], p2[2]],
            color='black', lw=1.2)

# Labels and formatting
ax.set_title("Vector Field F = xi + yj + zk and Divergence (∇·F = 3)", fontsize=14, color='darkblue')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_box_aspect([1, 1, 1])  # Equal aspect ratio

plt.tight_layout()
plt.show()
