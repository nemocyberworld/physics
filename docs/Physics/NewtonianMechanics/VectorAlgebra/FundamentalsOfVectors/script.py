# Representing and analyzing vectors using NumPy, with colors and explanations
import numpy as np
from colorama import Fore, Style, init

init(autoreset=True)  # Automatically reset color after each print

print(Fore.CYAN + "=== Vector Fundamentals with NumPy ===\n")

# 1. Zero Vector
print(Fore.YELLOW + "1. Zero Vector:")
print("A zero vector has no magnitude or direction. It is the additive identity for vectors.")
zero_vector = np.array([0, 0, 0])
print("   Vector:", Fore.GREEN + str(zero_vector))
print("   Magnitude:", Fore.MAGENTA + str(np.linalg.norm(zero_vector)) + "\n")

# 2. Unit Vectors
print(Fore.YELLOW + "2. Unit Vectors:")
print("Unit vectors have magnitude 1 and indicate direction along coordinate axes.")
unit_x = np.array([1, 0, 0])
unit_y = np.array([0, 1, 0])
unit_z = np.array([0, 0, 1])
print("   X-axis:", Fore.BLUE + str(unit_x))
print("   Y-axis:", Fore.BLUE + str(unit_y))
print("   Z-axis:", Fore.BLUE + str(unit_z) + "\n")

# 3. Position Vector
print(Fore.YELLOW + "3. Position Vector:")
print("A position vector locates a point in space relative to the origin.")
position_vector = np.array([3, 4, 0])
magnitude_pos = np.linalg.norm(position_vector)
print("   Vector:", Fore.GREEN + str(position_vector))
print("   Magnitude (length):", Fore.MAGENTA + str(round(magnitude_pos, 2)))  # Expected 5.0 (3-4-5 triangle)
direction_cosines = np.round(position_vector / magnitude_pos, 2)
print("   Direction cosines:", Fore.CYAN + str(direction_cosines) + "\n")

# 4. Reciprocal Vectors
print(Fore.YELLOW + "4. Reciprocal Vectors:")
print("Two vectors A and B are reciprocal if their dot product is 1: A · B = 1")
A = np.array([2, 0, 0])
B = np.array([0.5, 0, 0])
dot_AB = np.dot(A, B)
print("   Vector A:", Fore.GREEN + str(A))
print("   Vector B:", Fore.GREEN + str(B))
print("   A · B =", Fore.MAGENTA + str(dot_AB))

if np.isclose(dot_AB, 1.0):
    print(Fore.GREEN + "   ✅ A and B are reciprocal vectors.\n")
else:
    print(Fore.RED + "   ❌ A and B are not reciprocal.\n")
