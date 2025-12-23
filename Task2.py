# Task 2: Using math module

import math

# Ask user for input
num = float(input("Enter a number: "))

# Perform calculations
sqrt_val = math.sqrt(num)
log_val = math.log(num)   # natural log (base e)
sine_val = math.sin(num)  # sine in radians

# Display results
print(f"Square root of {num} is: {sqrt_val}")
print(f"Natural log of {num} is: {log_val}")
print(f"Sine of {num} radians is: {sine_val}")
