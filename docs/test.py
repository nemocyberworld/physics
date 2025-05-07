import numpy as np
from scipy.constants import hbar, pi

# Define the parameters
L = 1.0  # Length of the well
N = 100  # Number of grid points
x = np.linspace(0, L, N)  # Spatial grid
dx = x[1] - x[0]  # Grid spacing
V = np.zeros_like(x)  # Potential inside the well (zero potential)

# Hamiltonian matrix (discretized)
# Kinetic energy part (second derivative term)
T = - (hbar**2 / (2.0 * 9.11e-31)) * (np.diag(-2 * np.ones(N)) +
                                       np.diag(np.ones(N-1), 1) +
                                       np.diag(np.ones(N-1), -1)) / (dx**2)

# Potential energy part (diagonal matrix)
V_matrix = np.diag(V)

# Hamiltonian matrix (H = T + V)
H = T + V_matrix

# Solve the eigenvalue problem for the Hamiltonian
energies, wavefunctions = np.linalg.eigh(H)

# Print the first few energies
print("First few energies (in eV):")
for i in range(3):
    print(f"n={i+1}, E={energies[i]:.2f} eV")

# Optionally, print the wavefunctions if needed (for first few)
print("\nFirst few wavefunctions (normalized):")
for i in range(3):
    print(f"Wavefunction for n={i+1}:")
    print(wavefunctions[:, i])
