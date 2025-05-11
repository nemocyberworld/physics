import numpy as np
import matplotlib.pyplot as plt

def calculate_acceleration(u, v, t):
    """
    Calculate the acceleration using the formula:
    a = (v - u) / t
    """
    return (v - u) / t

def generate_velocity_graph(u, v, t):
    """
    Generate a velocity-time graph based on the given parameters:
    u = initial velocity
    v = final velocity
    t = time
    """
    # Time intervals
    time = np.linspace(0, t, 100)  # 100 points for smooth graph

    # Calculate the acceleration
    acceleration = calculate_acceleration(u, v, t)

    # Calculate the velocity at each time point
    velocity = u + acceleration * time

    # Plotting
    plt.figure(figsize=(8, 6))
    plt.plot(time, velocity, label='Velocity (km/h)', color='tab:blue', linewidth=2)

    # Adding labels and title
    plt.title("Velocity vs Time (Acceleration: {:.2f} km/h²)".format(acceleration), fontsize=14)
    plt.xlabel('Time (seconds)', fontsize=12)
    plt.ylabel('Velocity (km/h)', fontsize=12)
    plt.grid(True)
    plt.legend()

    # Show the plot
    plt.show()

def main():
    # User inputs
    print("Welcome to the Instantaneous Velocity and Acceleration Calculator!")
    u = float(input("Enter initial velocity (u) in km/h: "))
    v = float(input("Enter final velocity (v) in km/h: "))
    t = float(input("Enter time (t) in seconds: "))

    # Ensure that time is positive
    if t <= 0:
        print("Time should be a positive value!")
        return

    # Calculate the acceleration
    acceleration = calculate_acceleration(u, v, t)

    # Display the results
    print(f"\nCalculated Acceleration: {acceleration:.2f} km/h²")
    print(f"Average Speed: {(u + v) / 2:.2f} km/h")
    
    # Generate the velocity-time graph
    generate_velocity_graph(u, v, t)

if __name__ == "__main__":
    main()
