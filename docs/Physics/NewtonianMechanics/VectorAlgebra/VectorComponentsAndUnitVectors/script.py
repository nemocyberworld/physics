import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define vectors
A = np.array([3, 4, 5])  # Vector A
B = np.array([1, 2, 3])  # Vector B

# Function to compute magnitude of a vector
def magnitude(vector):
    return np.linalg.norm(vector)

# Function to compute the angle between two vectors
def angle_between_vectors(A, B):
    dot_product = np.dot(A, B)
    mag_A = magnitude(A)
    mag_B = magnitude(B)
    cos_theta = dot_product / (mag_A * mag_B)
    theta = np.arccos(cos_theta)
    return np.degrees(theta)

# Setup the figure and axis for the animation
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Setting the limits for the plot
ax.set_xlim([0, 6])
ax.set_ylim([0, 6])
ax.set_zlim([0, 6])

# Adding labels
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

# Create the quiver plot (arrows for vectors)
quiver_A = ax.quiver(0, 0, 0, A[0], A[1], A[2], color='b', label="Vector A (3i + 4j + 5k)", linewidth=2)
quiver_B = ax.quiver(0, 0, 0, B[0], B[1], B[2], color='r', label="Vector B (i + 2j + 3k)", linewidth=2)

# Function to draw the dotted lines representing vector components
def draw_dotted_line(start, end, color):
    ax.plot([start[0], end[0]], [start[1], end[1]], [start[2], end[2]], color=color, linestyle=':', linewidth=2)

# Add text annotations for the components of the vectors
text_A = ax.text(3.5, 0, 0, f"A = {A}", color='blue')
text_B = ax.text(0, 2.5, 0, f"B = {B}", color='red')

# Create the figure title and labels for magnitude and angle
title = ax.set_title(f"Angle between A and B: {angle_between_vectors(A, B):.2f}°", fontsize=12)

# Update function for animation
def update(frame):
    # Animate Vector A and Vector B
    ax.cla()  # Clear the axis
    ax.set_xlim([0, 6])
    ax.set_ylim([0, 6])
    ax.set_zlim([0, 6])

    # Re-add the vectors and components at each frame
    ax.quiver(0, 0, 0, A[0], A[1], A[2], color='b', label="Vector A", linewidth=2)
    ax.quiver(0, 0, 0, B[0], B[1], B[2], color='r', label="Vector B", linewidth=2)

    # Draw the dotted lines for the components of the vectors
    draw_dotted_line([0, 0, 0], [A[0], 0, 0], 'blue')  # X-component of A
    draw_dotted_line([A[0], 0, 0], [A[0], A[1], 0], 'blue')  # Y-component of A
    draw_dotted_line([A[0], A[1], 0], [A[0], A[1], A[2]], 'blue')  # Z-component of A

    draw_dotted_line([0, 0, 0], [B[0], 0, 0], 'red')  # X-component of B
    draw_dotted_line([B[0], 0, 0], [B[0], B[1], 0], 'red')  # Y-component of B
    draw_dotted_line([B[0], B[1], 0], [B[0], B[1], B[2]], 'red')  # Z-component of B

    # Re-add the text labels
    ax.text(3.5, 0, 0, f"A = {A}", color='blue')
    ax.text(0, 2.5, 0, f"B = {B}", color='red')

    # Update the title with the new angle between vectors
    title.set_text(f"Angle between A and B: {angle_between_vectors(A, B):.2f}°")
    
# Create the animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 2 * np.pi, 60), interval=100)

# Show the plot
plt.show()
