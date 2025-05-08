import numpy as np

# Torque from r and F
r = np.array([2, 1, 0])     # Position vector
F = np.array([0, 3, 5])     # Force vector

tau = np.cross(r, F)       # Compute torque
print("Torque =", tau)
