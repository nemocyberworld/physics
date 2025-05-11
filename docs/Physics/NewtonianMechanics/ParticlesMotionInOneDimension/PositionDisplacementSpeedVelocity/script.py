import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
velocity_x = 2.94  # Horizontal velocity (m/s) to achieve a range of 20 meters
initial_velocity_y = 10.14  # Initial vertical velocity (m/s) to achieve a height of 10 meters
gravity = 7.8  # m/s^2, acceleration due to gravity
time_interval = 0.1  # Time interval for the simulation (seconds)
total_time = 2.88  # Total time for the simulation (seconds) based on the calculated flight time

# Arrays for storing the positions and times
time = np.arange(0, total_time, time_interval)

# For car moving in a straight line
car_velocity = 6.94  # Using same horizontal velocity for car (optional)
car_position = car_velocity * time  # Position = velocity * time
car_displacement = car_position[-1]  # Displacement is final position

# For projectile motion (parabolic path)
projectile_position_x = velocity_x * time  # Horizontal motion (constant velocity)
projectile_position_y = initial_velocity_y * time - 0.5 * gravity * time**2  # Vertical motion (gravity effect)

# Create figure for plotting
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, total_time)
ax.set_ylim(0, 12)  # Adjusted to show the desired height (max 10 meters)

# Plotting car motion and projectile motion
ax.plot(time, car_position, label="Car Motion (Straight Line)", color='blue', linewidth=2)
ax.plot(time, projectile_position_y, label="Projectile Motion (Curved Path)", color='red', linewidth=2)

# Adding labels and title
ax.set_title("Position, Displacement, Average Velocity, and Average Speed")
ax.set_xlabel("Time (seconds)")
ax.set_ylabel("Position (meters)")
ax.legend()

# Adding text annotations
ax.text(0.5, 9, f"Car Displacement = {car_displacement:.2f} m", fontsize=12, color='blue')

# Function to animate the positions of the objects
def animate(frame):
    ax.clear()  # Clear the previous frame
    ax.set_xlim(0, total_time)
    ax.set_ylim(0, 12)  # Adjusted to show the desired height (max 10 meters)

    # Plot car motion and projectile motion dynamically
    ax.plot(time, car_position, label="Car Motion (Straight Line)", color='blue', linewidth=2)
    ax.plot(time, projectile_position_y, label="Projectile Motion (Curved Path)", color='red', linewidth=2)

    # Plot the moving objects
    ax.plot(time[frame], car_position[frame], 'bo', markersize=10)  # Car position
    ax.plot(time[frame], projectile_position_y[frame], 'ro', markersize=10)  # Projectile position

    # Update text with the current position
    ax.text(0.5, 9, f"Car Position: {car_position[frame]:.2f} m", fontsize=12, color='blue')
    ax.text(0.5, 8, f"Projectile Position: {projectile_position_y[frame]:.2f} m", fontsize=12, color='red')

    ax.set_title("Position, Displacement, Average Velocity, and Average Speed")
    ax.set_xlabel("Time (seconds)")
    ax.set_ylabel("Position (meters)")
    ax.legend()

# Create animation
ani = FuncAnimation(fig, animate, frames=len(time), interval=100, repeat=False)

# Show the plot
plt.show()
