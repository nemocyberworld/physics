import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# Set up the 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
ax.set_zlim([-3, 3])
ax.set_title("Understanding Vector Identities (BAC–CAB Rule)", fontsize=14)

# Define vectors
A = np.array([1, 0.5, 1])
B = np.array([0.5, 1, 0])
C = np.array([0, 1, 1])

# Compute vector operations
B_cross_C = np.cross(B, C)
AxBC = np.cross(A, B_cross_C)
BAC_CAB = np.dot(A, C)*B - np.dot(A, B)*C

quivers = []
texts = []

# Draw grid lines
def draw_grid_cube():
    grid_range = np.linspace(-3, 3, 7)
    for x in grid_range:
        for y in grid_range:
            ax.plot([-3, 3], [y, y], [x, x], color='grey', linewidth=0.5, alpha=0.5)
            ax.plot([x, x], [-3, 3], [y, y], color='grey', linewidth=0.5, alpha=0.5)
            ax.plot([y, y], [x, x], [-3, 3], color='grey', linewidth=0.5, alpha=0.5)

# Draw vector and add label
def draw_vector(vec, color, label, alpha=0.8):
    q = ax.quiver(0, 0, 0, vec[0], vec[1], vec[2], color=color, alpha=alpha)
    t = ax.text(vec[0]*1.1, vec[1]*1.1, vec[2]*1.1, label, color=color, fontsize=10)
    return q, t

# Update frame for animation
def update(frame):
    global quivers, texts
    for q in quivers:
        q.remove()
    for t in texts:
        t.remove()
    quivers.clear()
    texts.clear()

    ax.set_title(["Vectors A, B, and C",
                  "Cross Product: B × C",
                  "Triple Product: A × (B × C)",
                  "BAC–CAB Identity Result"][frame], fontsize=13)

    if frame == 0:
        q1, t1 = draw_vector(A, 'red', 'A')
        q2, t2 = draw_vector(B, 'green', 'B')
        q3, t3 = draw_vector(C, 'blue', 'C')
        quivers += [q1, q2, q3]
        texts += [t1, t2, t3]

    elif frame == 1:
        q1, t1 = draw_vector(B, 'green', 'B')
        q2, t2 = draw_vector(C, 'blue', 'C')
        q3, t3 = draw_vector(B_cross_C, 'magenta', 'B × C')
        quivers += [q1, q2, q3]
        texts += [t1, t2, t3]

    elif frame == 2:
        q1, t1 = draw_vector(A, 'red', 'A')
        q2, t2 = draw_vector(B_cross_C, 'magenta', 'B × C')
        q3, t3 = draw_vector(AxBC, 'cyan', 'A × (B × C)')
        quivers += [q1, q2, q3]
        texts += [t1, t2, t3]

    elif frame == 3:
        q1, t1 = draw_vector(A, 'red', 'A')
        q2, t2 = draw_vector(B, 'green', 'B')
        q3, t3 = draw_vector(C, 'blue', 'C')
        q4, t4 = draw_vector(BAC_CAB, 'orange', '(A·C)B - (A·B)C')
        quivers += [q1, q2, q3, q4]
        texts += [t1, t2, t3, t4]

draw_grid_cube()
ani = FuncAnimation(fig, update, frames=4, interval=2500, repeat=True)
plt.tight_layout()
plt.show()
