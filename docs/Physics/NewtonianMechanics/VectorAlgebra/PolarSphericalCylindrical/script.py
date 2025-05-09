import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Set up the figure
fig = plt.figure(figsize=(12, 8))

# Polar Coordinates Example: Plotting a circle
ax1 = fig.add_subplot(131)
theta = np.linspace(0, 2 * np.pi, 100)
r = 5
x = r * np.cos(theta)
y = r * np.sin(theta)
ax1.plot(x, y, label="r = 5", color="b")
ax1.set_title("Polar Coordinates: Circle (r = 5)")
ax1.set_xlabel("x-axis")
ax1.set_ylabel("y-axis")
ax1.axhline(0, color='black',linewidth=0.5)
ax1.axvline(0, color='black',linewidth=0.5)
ax1.grid(True)
ax1.set_aspect('equal', 'box')
ax1.legend()

# Cylindrical Coordinates Example: Plotting a cylinder
ax2 = fig.add_subplot(132, projection='3d')
z = np.linspace(-5, 5, 100)
theta_cyl = np.linspace(0, 2 * np.pi, 100)
theta_cyl, Z = np.meshgrid(theta_cyl, z)
r_cyl = 3
X_cyl = r_cyl * np.cos(theta_cyl)
Y_cyl = r_cyl * np.sin(theta_cyl)
ax2.plot_surface(X_cyl, Y_cyl, Z, color='c', alpha=0.7)

ax2.set_title("Cylindrical Coordinates: Cylinder")
ax2.set_xlabel("x-axis")
ax2.set_ylabel("y-axis")
ax2.set_zlabel("z-axis")
ax2.view_init(elev=30, azim=60)

# Spherical Coordinates Example: Plotting a sphere
ax3 = fig.add_subplot(133, projection='3d')

phi = np.linspace(0, np.pi, 100)
theta_sph = np.linspace(0, 2 * np.pi, 100)
phi, theta_sph = np.meshgrid(phi, theta_sph)

r_sph = 5
X_sph = r_sph * np.sin(phi) * np.cos(theta_sph)
Y_sph = r_sph * np.sin(phi) * np.sin(theta_sph)
Z_sph = r_sph * np.cos(phi)

ax3.plot_surface(X_sph, Y_sph, Z_sph, color='m', alpha=0.6)

ax3.set_title("Spherical Coordinates: Sphere")
ax3.set_xlabel("x-axis")
ax3.set_ylabel("y-axis")
ax3.set_zlabel("z-axis")
ax3.view_init(elev=30, azim=60)

# Show all plots
plt.tight_layout()
plt.show()

