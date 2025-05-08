import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Function to calculate the vector triple product
def vector_triple_product(A, B, C):
    return np.cross(A, np.cross(B, C))

# Create 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Define vectors for the example
A = np.array([2, 3, 1])
B = np.array([1, -2, 4])
C = np.array([3, 1, -5])

# Function to initialize the plot
def init():
    ax.set_xlim([0, 4])
    ax.set_ylim([-4, 4])
    ax.set_zlim([-6, 6])
    ax.set_xlabel('X', fontsize=12)
    ax.set_ylabel('Y', fontsize=12)
    ax.set_zlabel('Z', fontsize=12)
    ax.set_title("Vector Triple Product Animation", fontsize=16)
    ax.view_init(elev=20, azim=30)  # Set the initial view angle
    return []

# Function to update the plot in the animation
def update(frame):
    ax.cla()  # Clear the previous plot
    init()  # Redraw the axes

    # Interpolate the position of the vectors based on the frame
    A_interpolated = A * (frame / 100)
    B_interpolated = B * (frame / 100)
    C_interpolated = C * (frame / 100)

    # Calculate the cross product B x C and A x (B x C)
    B_cross_C = np.cross(B_interpolated, C_interpolated)
    A_cross_B_cross_C = vector_triple_product(A_interpolated, B_interpolated, C_interpolated)

    # Plot vectors A, B, and C
    ax.quiver(0, 0, 0, A_interpolated[0], A_interpolated[1], A_interpolated[2], color='r', label='A', linewidth=3)
    ax.quiver(0, 0, 0, B_interpolated[0], B_interpolated[1], B_interpolated[2], color='g', label='B', linewidth=3)
    ax.quiver(0, 0, 0, C_interpolated[0], C_interpolated[1], C_interpolated[2], color='b', label='C', linewidth=3)

    # Plot the cross product B x C
    ax.quiver(0, 0, 0, B_cross_C[0], B_cross_C[1], B_cross_C[2], color='purple', label='B x C', linewidth=2, linestyle='dashed')

    # Plot the vector triple product result A x (B x C)
    ax.quiver(0, 0, 0, A_cross_B_cross_C[0], A_cross_B_cross_C[1], A_cross_B_cross_C[2], color='orange', label='A x (B x C)', linewidth=3, linestyle='dotted')

    # Labels for the vectors
    ax.text(A_interpolated[0], A_interpolated[1], A_interpolated[2], 'A', color='r', fontsize=12)
    ax.text(B_interpolated[0], B_interpolated[1], B_interpolated[2], 'B', color='g', fontsize=12)
    ax.text(C_interpolated[0], C_interpolated[1], C_interpolated[2], 'C', color='b', fontsize=12)
    ax.text(B_cross_C[0], B_cross_C[1], B_cross_C[2], 'B x C', color='purple', fontsize=12)
    ax.text(A_cross_B_cross_C[0], A_cross_B_cross_C[1], A_cross_B_cross_C[2], 'A x (B x C)', color='orange', fontsize=12)

    # Update the legend dynamically
    ax.legend(loc='upper left')

    return []

# Create the animation
ani = FuncAnimation(fig, update, frames=100, init_func=init, blit=True, interval=50)

# Display the plot
plt.show()
