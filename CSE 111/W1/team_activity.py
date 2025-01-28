# DOCUMENTATION SECTION

"""
The time in seconds that a pendulum takes to swing back and
forth once is given by this formula:
             ____
            / h
    t = 2π / ----
          √  9.81

t is the time in seconds,
π is the constant PI, which is the ratio of the circumference
    of a circle divided by its diameter (use math.pi),
h is the length of the pendulum in meters.

Write a program that prompts a user to enter the length of a
pendulum in meters and then computes and prints the time in
seconds that it takes for that pendulum to swing back and forth.
"""

import math

# Ask the user for the length of the pendulum
h = float(input('Please Enter The Length Of The Pendulum (Meters): '))

# Calculate the time in seconds
t = 2 * math.pi * math.sqrt(h / 9.81)

# Print for the user the time in seconds
print(f'Time (seconds): {t:.2f}')

print()

# Base Length & Height From User of a Pyramid

# Ask the user for the base length of the pyramid
b = float(input('Please Enter The Base Length Of The Pyramid (Meters): '))

# Ask the user for the height of the pyramid
h = float(input('Please Enter The Height Of The Pyramid (Meters): '))

# Calculate the volume of the pyramid
v = (b ** 2) * h / 3

# Print for the user the volume of the pyramid
print(f'Volume (cubic meters): {v:.2f}')

