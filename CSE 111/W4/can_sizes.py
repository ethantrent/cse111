"""
Computes and prints the storage efficiency for each of the following 12 steel can sizes
volume = π radius2 height
surface_area = 2π radius (radius + height)
"""

# Name	Radius (cm)	Height (cm)	Cost per can ($)
#1 Picnic	6.83	10.16	0.28
#1 Tall	7.78	11.91	0.43
#2	8.73	11.59	0.45
#2.5	10.32	11.91	0.61
#3 Cylinder	10.79	17.78	0.86
#5	13.02	14.29	0.83
#6Z	5.40	8.89	0.22
#8Z short	6.83	7.62	0.26
#10	15.72	17.78	1.53
#211	6.83	12.38	0.34
#300	7.62	11.27	0.38
#303	8.10	11.11	0.42

import math

def main():
    can_sizes = [
                    # radius, height
        ("#1 Picnic", 6.83, 10.16),
        ("#1 Tall", 7.78, 11.91),
        ("#2", 8.73, 11.59),
        ("#2.5", 10.32, 11.91),
        ("#3 Cylinder", 10.79, 17.78),
        ("#5", 13.02, 14.29),
        ("#6Z", 5.40, 8.89),
        ("#8Z short", 6.83, 7.62),
        ("#10", 15.72, 17.78),
        ("#211", 6.83, 12.38),
        ("#300", 7.62, 11.27),
        ("#303", 8.10, 11.11)
    ]

    for name, radius, height in can_sizes:
        efficiency = compute_storage_efficiency(radius, height)
        print(f"{name}: {efficiency:.2f}")

def compute_volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume
def compute_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

# Add another function named compute_storage_efficiency to your program. 
# This function should call the compute_volume and compute_surface_area functions and 
# then compute and return the storage efficiency of a steel can size. 
# Replace code in the main function with a call to the compute_storage_efficiency function as appropriate.

def compute_storage_efficiency(radius, height):
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    efficiency = volume / surface_area
    return efficiency

main ()