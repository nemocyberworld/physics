import numpy as np
import matplotlib.pyplot as plt

# Time (seconds)
t = np.linspace(0, 10, 100)

# Speeds in m/s
v_car = 20  # Speed of car in ground frame
v_train = 10  # Speed of train in ground frame

# Position of car in ground frame
x_car_ground = v_car * t

# Position of car in train's frame
x_car_train = (v_car - v_train) * t

# Plotting
plt.plot(t, x_car_ground, label='Car in Ground Frame')
plt.plot(t, x_car_train, label='Car in Train Frame', linestyle='--')
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.title('Motion in Different Frames of Reference')
plt.legend()
plt.grid(True)
plt.show()
