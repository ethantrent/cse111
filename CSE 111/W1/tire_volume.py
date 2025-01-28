"""
Write a Python program named tire_volume.py that reads from 
the keyboard the three numbers for a tire and computes and outputs 
the volume of space inside that tire.
"""

import math

w = int(input('Please Enter The Width Of The Tire (Millimeters): '))
a = int(input('Please Enter The Aspect Ratio Of The Tire: '))
d = int(input('Please Enter The Diameter Of The Tire (Inches): '))
v = (math.pi * w**2 * a * (w * a + 2540 * d)) / (10000000000)

print(f'\nThe approximate volume of the tire is {v:.2f} liters.')