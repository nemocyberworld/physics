# import numpy as np
# import matplotlib.pyplot as plt

# # Time values
# t = np.linspace(0, 5, 100)

# # Define a position vector function: r(t) = [3t^2, 2t, 5]
# x = 3 * t**2
# y = 2 * t
# z = np.full_like(t, 5)

# # Velocity: v(t) = [6t, 2, 0]
# vx = 6 * t
# vy = np.full_like(t, 2)
# vz = np.zeros_like(t)

# # Acceleration: a(t) = [6, 0, 0]
# ax = np.full_like(t, 6)
# ay = np.zeros_like(t)
# az = np.zeros_like(t)

# # Plot the position vector components
# fig, axs = plt.subplots(3, 1, figsize=(10, 10), sharex=True)
# fig.suptitle("Vector Differentiation: Position, Velocity, and Acceleration", fontsize=16, color='navy')

# # Position
# axs[0].plot(t, x, label='x(t) = 3t²', color='blue')
# axs[0].plot(t, y, label='y(t) = 2t', color='green')
# axs[0].plot(t, z, label='z(t) = 5', color='red')
# axs[0].set_ylabel('Position')
# axs[0].legend()
# axs[0].grid(True)

# # Velocity
# axs[1].plot(t, vx, label="vx(t) = 6t", color='blue')
# axs[1].plot(t, vy, label="vy(t) = 2", color='green')
# axs[1].plot(t, vz, label="vz(t) = 0", color='red')
# axs[1].set_ylabel('Velocity')
# axs[1].legend()
# axs[1].grid(True)

# # Acceleration
# axs[2].plot(t, ax, label="ax(t) = 6", color='blue')
# axs[2].plot(t, ay, label="ay(t) = 0", color='green')
# axs[2].plot(t, az, label="az(t) = 0", color='red')
# axs[2].set_ylabel('Acceleration')
# axs[2].set_xlabel('Time (s)')
# axs[2].legend()
# axs[2].grid(True)

# plt.tight_layout(rect=[0, 0.03, 1, 0.95])
# plt.show()
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Initial parameters
a_init = 3
b_init = 2
c_init = 5

# Time array
t = np.linspace(0, 5, 200)

# Create figure and axes
fig, axs = plt.subplots(3, 1, figsize=(10, 10), sharex=True)
plt.subplots_adjust(left=0.1, bottom=0.25, hspace=0.4)
fig.suptitle("Interactive Vector Differentiation", fontsize=16, color='navy')

# Initial vector functions
def compute_vectors(a, b, c):
    x = a * t**2
    y = b * t
    z = np.full_like(t, c)

    vx = 2 * a * t
    vy = np.full_like(t, b)
    vz = np.zeros_like(t)

    ax = np.full_like(t, 2 * a)
    ay = np.zeros_like(t)
    az = np.zeros_like(t)

    return x, y, z, vx, vy, vz, ax, ay, az

# Initial computation
x, y, z, vx, vy, vz, ax, ay, az = compute_vectors(a_init, b_init, c_init)

# Plot initial data
pos_x, = axs[0].plot(t, x, label='x(t) = at²', color='blue')
pos_y, = axs[0].plot(t, y, label='y(t) = bt', color='green')
pos_z, = axs[0].plot(t, z, label='z(t) = c', color='red')
axs[0].set_ylabel('Position')
axs[0].legend()
axs[0].grid(True)

vel_x, = axs[1].plot(t, vx, label="vx(t)", color='blue')
vel_y, = axs[1].plot(t, vy, label="vy(t)", color='green')
vel_z, = axs[1].plot(t, vz, label="vz(t)", color='red')
axs[1].set_ylabel('Velocity')
axs[1].legend()
axs[1].grid(True)

acc_x, = axs[2].plot(t, ax, label="ax(t)", color='blue')
acc_y, = axs[2].plot(t, ay, label="ay(t)", color='green')
acc_z, = axs[2].plot(t, az, label="az(t)", color='red')
axs[2].set_ylabel('Acceleration')
axs[2].set_xlabel('Time (s)')
axs[2].legend()
axs[2].grid(True)

# Sliders for parameters a, b, c
axcolor = 'lightgoldenrodyellow'
ax_a = plt.axes([0.15, 0.15, 0.7, 0.03], facecolor=axcolor)
ax_b = plt.axes([0.15, 0.1, 0.7, 0.03], facecolor=axcolor)
ax_c = plt.axes([0.15, 0.05, 0.7, 0.03], facecolor=axcolor)

slider_a = Slider(ax_a, 'a (x coeff)', 0.0, 10.0, valinit=a_init)
slider_b = Slider(ax_b, 'b (y coeff)', 0.0, 10.0, valinit=b_init)
slider_c = Slider(ax_c, 'c (z const)', 0.0, 10.0, valinit=c_init)

# Update function
def update(val):
    a = slider_a.val
    b = slider_b.val
    c = slider_c.val
    x, y, z, vx, vy, vz, ax_vals, ay_vals, az_vals = compute_vectors(a, b, c)

    pos_x.set_ydata(x)
    pos_y.set_ydata(y)
    pos_z.set_ydata(z)

    vel_x.set_ydata(vx)
    vel_y.set_ydata(vy)
    vel_z.set_ydata(vz)

    acc_x.set_ydata(ax_vals)
    acc_y.set_ydata(ay_vals)
    acc_z.set_ydata(az_vals)

    fig.canvas.draw_idle()

# Connect sliders to update function
slider_a.on_changed(update)
slider_b.on_changed(update)
slider_c.on_changed(update)

plt.show()
