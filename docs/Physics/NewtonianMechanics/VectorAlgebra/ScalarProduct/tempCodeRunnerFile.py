import numpy as np
import matplotlib.pyplot as plt

# Function to plot vectors
def plot_vectors(A, B, ax, label_A="A", label_B="B"):
    ax.quiver(0, 0, A[0], A[1], angles='xy', scale_units='xy', scale=1, color='r', label=label_A)
    ax.quiver(0, 0, B[0], B[1], angles='xy', scale_units='xy', scale=1, color='b', label=label_B)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_aspect('equal')
    ax.grid(True)
    
    # Set grid to show one unit at a time
    ax.set_xticks(np.arange(-5, 6, 1))
    ax.set_yticks(np.arange(-5, 6, 1))

    ax.axhline(0, color='black',linewidth=1)
    ax.axvline(0, color='black',linewidth=1)
    ax.legend()

# Function to calculate and display dot product and angle
def compute_and_display_dot_product(A, B):
    dot_product = np.dot(A, B)
    magnitude_A = np.linalg.norm(A)
    magnitude_B = np.linalg.norm(B)
    cos_theta = dot_product / (magnitude_A * magnitude_B)
    angle_rad = np.arccos(cos_theta)
    angle_deg = np.degrees(angle_rad)

    print(f"Dot Product of A and B: {dot_product}")
    print(f"Angle between A and B: {angle_deg:.2f} degrees")

    return dot_product, angle_deg

# Example 1: Simple Dot Product
A1 = np.array([2, 3])
B1 = np.array([4, 1])

fig, ax = plt.subplots(1, 2, figsize=(12, 6))

# Plot vectors A1 and B1
plot_vectors(A1, B1, ax[0], label_A="A1", label_B="B1")
ax[0].set_title("Example 1: Vectors A1 and B1")

# Compute and display the dot product
compute_and_display_dot_product(A1, B1)

# Example 2: Perpendicular Vectors
A2 = np.array([1, 0])
B2 = np.array([0, 1])

# Plot vectors A2 and B2
plot_vectors(A2, B2, ax[1], label_A="A2", label_B="B2")
ax[1].set_title("Example 2: Perpendicular Vectors A2 and B2")

# Compute and display the dot product
compute_and_display_dot_product(A2, B2)

plt.tight_layout()
plt.show()

# Example 3: Angle Between Two Vectors
A3 = np.array([3, 4])
B3 = np.array([4, -3])

# Compute and display dot product and angle
dot_product_3, angle_3 = compute_and_display_dot_product(A3, B3)

# Visualize the vectors
fig, ax = plt.subplots(figsize=(6, 6))
plot_vectors(A3, B3, ax, label_A="A3", label_B="B3")
ax.set_title(f"Example 3: Angle Between Vectors A3 and B3\nAngle = {angle_3:.2f} degrees")
plt.show()

# Example 4: Dot Product and Work Done by a Force
A4 = np.array([5, 0])  # Force vector (along x-axis)
B4 = np.array([2, 3])  # Displacement vector (in any direction)

# Compute and display dot product (Work done)
work_done, _ = compute_and_display_dot_product(A4, B4)
print(f"\nWork Done by the Force: {work_done:.2f} Joules")
