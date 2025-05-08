import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from matplotlib import rcParams

# Improve appearance
rcParams['axes.titlesize'] = 14
rcParams['axes.labelsize'] = 12

# Setup figure and 3D axis
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Vector A (fixed)
A = np.array([2, 0, 0])
origin = np.array([0, 0, 0])

# Pre-initialize text objects (top-left and top-right)
angle_text = fig.text(0.02, 0.92, '', fontsize=12, color='blue')  # top-left
magnitude_text = fig.text(0.75, 0.92, '', fontsize=12, color='red')  # top-right

def update(frame):
    ax.cla()

    # Axis settings
    ax.set_xlim([-3, 3])
    ax.set_ylim([-3, 3])
    ax.set_zlim([-3, 3])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Vector Cross Product Visualization')

    # Update rotating vector B
    theta = np.radians(frame)
    B = np.array([np.cos(theta), np.sin(theta), np.sin(theta / 2)])
    C = np.cross(A, B)

    # Compute angle in degrees
    dot = np.dot(A, B)
    angle_rad = np.arccos(np.clip(dot / (np.linalg.norm(A) * np.linalg.norm(B)), -1.0, 1.0))
    angle_deg = np.degrees(angle_rad)
    magnitude = np.linalg.norm(C)

    # Plot vectors
    ax.quiver(*origin, *A, color='blue', label='Vector A', arrow_length_ratio=0.1)
    ax.quiver(*origin, *B, color='green', label='Vector B', arrow_length_ratio=0.1)
    ax.quiver(*origin, *C, color='red', label='A × B', arrow_length_ratio=0.1)

    # Update separate text boxes
    angle_text.set_text(f"θ ≈ {angle_deg:.1f}°")
    magnitude_text.set_text(f"|A × B| ≈ {magnitude:.2f}")

    ax.legend(loc='upper left')

# Create animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 2), interval=100)

plt.tight_layout()
plt.show()
