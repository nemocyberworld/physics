import numpy as np
import matplotlib.pyplot as plt

# Define vectors
a = np.array([1, 0])
b = np.array([0, 1])
c = np.array([1, 1])

# Check orthogonality
print("Dot product of a and b:", np.dot(a, b))
print("Norm of a:", np.linalg.norm(a))
print("Norm of b:", np.linalg.norm(b))

# Plotting
plt.figure(figsize=(6,6))
plt.quiver(0, 0, a[0], a[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Vector a')
plt.quiver(0, 0, b[0], b[1], angles='xy', scale_units='xy', scale=1, color='red', label='Vector b')
plt.quiver(0, 0, c[0], c[1], angles='xy', scale_units='xy', scale=1, color='green', label='Vector c')

plt.xlim(-1, 2)
plt.ylim(-1, 2)
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.title('Visualizing Orthogonal and Non-Orthogonal Vectors')
plt.show()