import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Slider
from mpl_toolkits.mplot3d.art3d import Poly3DCollection  # Add this import

# Function to compute the scalar triple product
def scalar_triple_product(A, B, C):
    return np.dot(A, np.cross(B, C))

# Initialize vectors
A = np.array([1, 2, 3])
B = np.array([4, 5, 6])
C = np.array([7, 8, 9])

# Create the figure and 3D axis
fig = plt.figure(figsize=(12, 10))  # Adjust figure size
ax = fig.add_subplot(111, projection='3d')

# Function to plot vectors and parallelepiped
def plot_vectors(ax, A, B, C):
    ax.quiver(0, 0, 0, A[0], A[1], A[2], color='r', label='A', linewidth=2)
    ax.quiver(0, 0, 0, B[0], B[1], B[2], color='g', label='B', linewidth=2)
    ax.quiver(0, 0, 0, C[0], C[1], C[2], color='b', label='C', linewidth=2)

    # Parallelepiped faces using Poly3DCollection
    vertices = np.array([[0, 0, 0], A, B, C, A + B, A + C, B + C, A + B + C])
    faces = [
        [vertices[0], vertices[1], vertices[4], vertices[2]],  # ABC plane
        [vertices[0], vertices[1], vertices[5], vertices[3]],  # AB plane
        [vertices[0], vertices[2], vertices[3], vertices[6]],  # AC plane
        [vertices[0], vertices[3], vertices[5], vertices[6]],  # BC plane
        [vertices[1], vertices[4], vertices[7], vertices[5]],  # A + B plane
        [vertices[2], vertices[3], vertices[7], vertices[6]],  # A + C plane
    ]
    ax.add_collection3d(Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='r', alpha=0.3))

    ax.set_xlim([0, 10])
    ax.set_ylim([0, 10])
    ax.set_zlim([0, 10])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend()

# Update function for the animation
def update(val):
    global A, B, C

    # Update vector components from sliders
    A = np.array([slider_Ax.val, slider_Ay.val, slider_Az.val])
    B = np.array([slider_Bx.val, slider_By.val, slider_Bz.val])
    C = np.array([slider_Cx.val, slider_Cy.val, slider_Cz.val])

    # Clear previous plot and plot new vectors
    ax.clear()
    plot_vectors(ax, A, B, C)

    # Compute scalar triple product
    volume = scalar_triple_product(A, B, C)
    
    # Update scalar triple product display
    ax.text2D(0.05, 0.95, f'Scalar Triple Product: {volume:.2f}', transform=ax.transAxes, fontsize=14, color='black')

    # Redraw the figure
    fig.canvas.draw_idle()

# Create sliders for interactive vector components
ax_slider_Ax = plt.axes([0.2, 0.02, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_slider_Ay = plt.axes([0.2, 0.06, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_slider_Az = plt.axes([0.2, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')

ax_slider_Bx = plt.axes([0.2, 0.14, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_slider_By = plt.axes([0.2, 0.18, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_slider_Bz = plt.axes([0.2, 0.22, 0.65, 0.03], facecolor='lightgoldenrodyellow')

ax_slider_Cx = plt.axes([0.2, 0.26, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_slider_Cy = plt.axes([0.2, 0.3, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_slider_Cz = plt.axes([0.2, 0.34, 0.65, 0.03], facecolor='lightgoldenrodyellow')

# Sliders for vector components
slider_Ax = Slider(ax_slider_Ax, 'Ax', -10, 10, valinit=A[0], valstep=0.1)
slider_Ay = Slider(ax_slider_Ay, 'Ay', -10, 10, valinit=A[1], valstep=0.1)
slider_Az = Slider(ax_slider_Az, 'Az', -10, 10, valinit=A[2], valstep=0.1)

slider_Bx = Slider(ax_slider_Bx, 'Bx', -10, 10, valinit=B[0], valstep=0.1)
slider_By = Slider(ax_slider_By, 'By', -10, 10, valinit=B[1], valstep=0.1)
slider_Bz = Slider(ax_slider_Bz, 'Bz', -10, 10, valinit=B[2], valstep=0.1)

slider_Cx = Slider(ax_slider_Cx, 'Cx', -10, 10, valinit=C[0], valstep=0.1)
slider_Cy = Slider(ax_slider_Cy, 'Cy', -10, 10, valinit=C[1], valstep=0.1)
slider_Cz = Slider(ax_slider_Cz, 'Cz', -10, 10, valinit=C[2], valstep=0.1)

# Link sliders to update function
slider_Ax.on_changed(update)
slider_Ay.on_changed(update)
slider_Az.on_changed(update)

slider_Bx.on_changed(update)
slider_By.on_changed(update)
slider_Bz.on_changed(update)

slider_Cx.on_changed(update)
slider_Cy.on_changed(update)
slider_Cz.on_changed(update)

# Adjust layout to ensure sliders are below the 3D plot
plt.subplots_adjust(bottom=0.4)  # Adjust bottom margin to create space for sliders

# Initial plot setup
plot_vectors(ax, A, B, C)
plt.show()
