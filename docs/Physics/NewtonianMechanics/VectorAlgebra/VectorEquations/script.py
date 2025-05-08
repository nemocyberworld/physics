import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Parameters
t_vals = np.linspace(0, 10, 200)

# 1. Straight Line: r = a + tb
a = np.array([0, 0, 0])
b = np.array([1, 2, 1])
line_points = np.array([a + t * b for t in t_vals])

# 2. Plane: r = p + su + tv
p = np.array([0, 0, 0])
u = np.array([1, 0, 0])
v = np.array([0, 1, 1])
s_vals = np.linspace(-2, 2, 10)
t_vals_plane = np.linspace(-2, 2, 10)
S, T = np.meshgrid(s_vals, t_vals_plane)
plane_points = p[:, None, None] + S * u[:, None, None] + T * v[:, None, None]

# 3. Helix: r(t) = (cos(t), sin(t), t)
helix_points = np.array([[np.cos(t), np.sin(t), t] for t in t_vals])

def update(frame):
    ax.cla()
    ax.set_title("Vector Equation Animations")
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_zlim(-2, 12)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    # Draw Line Path
    ax.plot(line_points[:,0], line_points[:,1], line_points[:,2], color='blue', label="Line: a + tb")
    ax.quiver(*a, *(line_points[frame] - a), color='blue', length=1, normalize=True)

    # Draw Plane
    ax.plot_surface(plane_points[0], plane_points[1], plane_points[2], color='orange', alpha=0.4, edgecolor='none')
    ax.text(*p, "Plane Origin", color='black')

    # Draw Helix
    ax.plot(helix_points[:frame,0], helix_points[:frame,1], helix_points[:frame,2], color='purple', label="Helix: (cos t, sin t, t)")
    ax.quiver(0, 0, 0, *helix_points[frame], color='purple', linewidth=2)

    ax.legend()

ani = FuncAnimation(fig, update, frames=len(t_vals), interval=50)
plt.show()
