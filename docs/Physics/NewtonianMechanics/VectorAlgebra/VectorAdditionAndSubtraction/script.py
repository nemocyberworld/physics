import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.lines import Line2D

# --- Define vectors ---
A = np.array([5, 3])
B = np.array([3, 5])
combo = 2 * A - 1.5 * B
origin = np.array([0, 0])
x_limits = (-2, 10)
y_limits = (-2, 10)
frames_per_phase = 40
pause_frames = 10

# --- Setup figure ---
fig, ax = plt.subplots(figsize=(7, 7))
ax.set_xlim(x_limits)
ax.set_ylim(y_limits)
ax.axhline(0, color='gray', linewidth=0.5)
ax.axvline(0, color='gray', linewidth=0.5)
ax.set_aspect('equal')
ax.grid(True)

# --- Initialize quivers and labels ---
quiv_A = ax.quiver(*origin, 0, 0, angles='xy', scale_units='xy', scale=1, color='red')
quiv_B = ax.quiver(*origin, 0, 0, angles='xy', scale_units='xy', scale=1, color='green')
quiv_R = ax.quiver(*origin, 0, 0, angles='xy', scale_units='xy', scale=1, color='blue', width=0.01)

label_A = ax.text(0, 0, '', color='red')
label_B = ax.text(0, 0, '', color='green')
label_R = ax.text(0, 0, '', color='blue', fontweight='bold')
title = ax.set_title("")

# --- Dotted helper lines ---
helper_line1, = ax.plot([], [], 'k--', linewidth=1)
helper_line2, = ax.plot([], [], 'k--', linewidth=1)

# --- Update Function ---
def update(frame):
    phase = frame // (frames_per_phase + pause_frames)
    local_frame = frame % (frames_per_phase + pause_frames)
    t = min(local_frame / frames_per_phase, 1)

    # Reset vector origins
    quiv_B.set_offsets(origin)
    label_A.set_text('')
    label_B.set_text('')
    label_R.set_text('')
    helper_line1.set_data([], [])
    helper_line2.set_data([], [])

    if phase == 0:
        # --- Vector Addition ---
        title.set_text("Vector Addition: A + B")
        a_vec = t * A
        b_vec = t * B
        r_vec = t * (A + B)
        quiv_A.set_UVC(*a_vec)
        quiv_B.set_UVC(*b_vec)
        quiv_B.set_offsets(A * t)
        quiv_R.set_UVC(*r_vec)
        quiv_R.set_offsets(origin)

        label_A.set_position(a_vec * 0.5)
        label_B.set_position(A * t + b_vec * 0.5)
        label_R.set_position(r_vec * 0.5)
        label_A.set_text('A')
        label_B.set_text('B (from tip of A)')
        label_R.set_text('A + B')

        # Dotted lines from origin to A and from A to A+B
        helper_line1.set_data([0, a_vec[0]], [0, a_vec[1]])
        helper_line2.set_data([a_vec[0], r_vec[0]], [a_vec[1], r_vec[1]])

    elif phase == 1:
        # --- Vector Subtraction ---
        title.set_text("Vector Subtraction: A - B")
        a_vec = t * A
        b_vec = t * B
        r_vec = t * (A - B)
        quiv_A.set_UVC(*a_vec)
        quiv_B.set_UVC(*b_vec)
        quiv_B.set_offsets(origin)
        quiv_R.set_UVC(*r_vec)
        quiv_R.set_offsets(origin)

        label_A.set_position(a_vec * 0.5)
        label_B.set_position(b_vec * 0.5)
        label_R.set_position(r_vec * 0.5)
        label_A.set_text('A')
        label_B.set_text('B')
        label_R.set_text('A - B')

        # Dotted line from tip of B to tip of A (shows subtraction logic)
        helper_line1.set_data([b_vec[0], a_vec[0]], [b_vec[1], a_vec[1]])

    elif phase == 2:
        # --- Linear Combination ---
        title.set_text("Linear Combination: 2A - 1.5B")
        a_vec = t * (2 * A)
        b_vec = t * (1.5 * B)
        r_vec = t * combo
        quiv_A.set_UVC(*a_vec)
        quiv_B.set_UVC(*b_vec)
        quiv_B.set_offsets(origin)
        quiv_R.set_UVC(*r_vec)
        quiv_R.set_offsets(origin)

        label_A.set_position(a_vec * 0.5)
        label_B.set_position(b_vec * 0.5)
        label_R.set_position(r_vec * 0.5)
        label_A.set_text('2A')
        label_B.set_text('1.5B')
        label_R.set_text('2A - 1.5B')

        # Dotted lines: show combo path visually
        helper_line1.set_data([0, a_vec[0]], [0, a_vec[1]])  # from origin to 2A
        helper_line2.set_data([a_vec[0], r_vec[0]], [a_vec[1], r_vec[1]])  # 2A to final

# --- Create animation ---
total_phases = 3
total_frames = total_phases * (frames_per_phase + pause_frames)
ani = FuncAnimation(fig, update, frames=total_frames, interval=100, repeat=True)

plt.show()
