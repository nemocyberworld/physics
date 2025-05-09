import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- Line Integral Example: Work Done ---
def line_integral_example():
    # Define the force field F(x, y) = x * i + y * j
    def force(x, y):
        return np.array([x, y])
    
    # Define the path C from (0, 0) to (1, 1) where x = y
    t = np.linspace(0, 1, 100)
    x = t
    y = t
    
    # Calculate the differential displacement dr = dx i + dy j
    dx = np.gradient(x)
    dy = np.gradient(y)
    dr = np.vstack((dx, dy)).T
    
    # Calculate the dot product F(x, y) . dr
    F_dot_dr = (force(x, y)[0] * dr[:, 0] + force(x, y)[1] * dr[:, 1])
    
    # Perform the integration (numerical summation)
    work_done = np.sum(F_dot_dr)
    
    # Plotting the path and force field
    fig, ax = plt.subplots()
    ax.quiver(x, y, force(x, y)[0], force(x, y)[1], color='blue', label='Force field', alpha=0.5)
    ax.plot(x, y, color='green', label='Path of motion')
    ax.set_title("Line Integral Example: Work Done")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()
    plt.grid(True)
    plt.show()
    
    return work_done

# --- Surface Integral Example: Electric Flux ---
def surface_integral_example():
    # Define the electric field E = E * z-hat
    E = 1  # Constant electric field in z-direction
    A = 1  # Area of the flat surface in the xy-plane
    
    # Electric flux is simply E * A for a uniform field
    flux = E * A
    
    # Plotting the surface and electric field vectors
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = np.linspace(0, 1, 10)
    y = np.linspace(0, 1, 10)
    X, Y = np.meshgrid(x, y)
    Z = np.zeros_like(X)
    
    ax.quiver(X, Y, Z, np.zeros_like(X), np.zeros_like(Y), np.ones_like(Z), color='red', length=0.1)
    ax.set_title("Surface Integral Example: Electric Flux")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.show()
    
    return flux

# --- Volume Integral Example: Mass in a Density Field ---
def volume_integral_example():
    # Define the density function ρ(x, y, z) = x * y * z
    def density(x, y, z):
        return x * y * z
    
    # Use a simple grid for integration over the unit cube (0 to 1 for all axes)
    x = np.linspace(0, 1, 10)
    y = np.linspace(0, 1, 10)
    z = np.linspace(0, 1, 10)
    
    # Create a meshgrid for x, y, z
    X, Y, Z = np.meshgrid(x, y, z)
    
    # Calculate the density at each point in the grid
    rho = density(X, Y, Z)
    
    # Numerical approximation of the volume integral (triple sum)
    volume = np.sum(rho) * (x[1] - x[0]) * (y[1] - y[0]) * (z[1] - z[0])
    
    # Plotting the density function over the cube
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(X, Y, Z, c=rho, cmap='viridis')
    ax.set_title("Volume Integral Example: Mass in a Density Field")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.show()
    
    return volume

# --- Main Execution ---
if __name__ == "__main__":
    print("Line Integral (Work Done) Result:", line_integral_example())
    print("Surface Integral (Electric Flux) Result:", surface_integral_example())
    print("Volume Integral (Mass) Result:", volume_integral_example())
