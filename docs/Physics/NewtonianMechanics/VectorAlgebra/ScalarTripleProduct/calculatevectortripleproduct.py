import numpy as np
import time

def slow_print(text, delay=0.1):
    """Simulate slow print effect"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Move to the next line after the slow print

def vector_triple_product(A, B, C):
    """Calculates the vector triple product (A x B) . C"""
    A = np.array(A)
    B = np.array(B)
    C = np.array(C)
    
    # Calculate the cross product of A and B
    cross_product = np.cross(A, B)
    
    # Calculate the dot product of (A x B) with C
    triple_product = np.dot(cross_product, C)
    
    return triple_product

def get_vector_input(vector_name):
    """Function to get vector input from the user with validation"""
    while True:
        try:
            print(f"Enter the components of vector {vector_name}:")
            x = float(input("x: "))
            y = float(input("y: "))
            z = float(input("z: "))
            return [x, y, z]
        except ValueError:
            print("\n[WARNING] Invalid input! Please enter valid numerical values for x, y, and z.")

# Get input vectors from the user
A = get_vector_input('A')
B = get_vector_input('B')
C = get_vector_input('C')

# Calculate the vector triple product
result = vector_triple_product(A, B, C)

# Displaying the results with slow print
try:
    slow_print(f"Calculating vector triple product...", 0.1)
    slow_print(f"\nVector A: {A}", 0.1)
    slow_print(f"Vector B: {B}", 0.1)
    slow_print(f"Vector C: {C}", 0.1)
    slow_print(f"\nThe vector triple product is: {result}", 0.1)
except KeyboardInterrupt:
    print("\nProcess interrupted. Exiting gracefully.")
