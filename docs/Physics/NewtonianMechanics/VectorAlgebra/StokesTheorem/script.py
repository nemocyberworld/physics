import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# Create a mesh grid
x = np.linspace(-2, 2, 20)
y = np.linspace(-2, 2, 20)
X, Y = np.meshgrid(x, y)

# Define the vector field F = (y, -x, 0)
U = Y
V = -X
W = np.zeros_like(U)  # No Z component

# Compute vector magnitudes for coloring
magnitude = np.sqrt(U**2 + V**2)
norm = plt.Normalize(magnitude.min(), magnitude.max())
colors = cm.viridis(norm(magnitude))

# Create Z=0 plane for 3D quiver
Z = np.zeros_like(X)

# Set up 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Flatten data for quiver
ax.quiver(
    X, Y, Z,
    U, V, W,
    length=0.2,
    normalize=True,
    color=colors.reshape(-1, 4)
)

# Labels and view
ax.set_title("Vector Field F = (y, -x, 0)", fontsize=16, color='navy')
ax.set_xlabel('X-axis', fontsize=12)
ax.set_ylabel('Y-axis', fontsize=12)
ax.set_zlabel('Z-axis (Zero)', fontsize=12)
ax.view_init(elev=20, azim=60)

plt.tight_layout()
plt.show()
