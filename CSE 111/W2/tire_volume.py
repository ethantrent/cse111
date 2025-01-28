"""
Gets the current date from the computer’s operating system.
Opens a text file named volumes.txt for appending.
Appends to the end of the volumes.txt file one line of text that contains the following five values:
current date
width of the tire
aspect ratio of the tire
diameter of the wheel
volume of the tire
"""

# STRETCH
# After your program prints the tire volume to the terminal window, your program should ask the user
# if she wants to buy tires with the dimensions that she entered. If the user answers “yes”, your program should ask
# for her phone number and store her phone number in the volumes.txt file.

import math

# Get the current date from the computer's operating system.
from datetime import datetime
current_date = datetime.now()

# print(f"{current_date:%Y-%m-%d}") prints the current date in the format YYYY-MM-DD.

# Open a text file named volumes.txt for appending.
    
w = int(input('Please Enter The Width Of The Tire (Millimeters): '))
a = int(input('Please Enter The Aspect Ratio Of The Tire: '))
d = int(input('Please Enter The Diameter Of The Tire (Inches): '))
v = (math.pi * w**2 * a * (w * a + 2540 * d)) / (10000000000)

# Open a text file named volumes.txt for appending.
with open("volumes.txt", "at") as volumes_file:
    # Initialize phone_number with an empty string
    phone_number = ''
    # Ask the user if she wants to buy tires with the dimensions that she entered.
    buy = input('Would you like to buy tires with the dimensions you entered? (yes/no): ').strip().lower()
    if buy == 'yes':
        phone_number = input('Please Enter Your Phone Number: ')
        print('Thank you. Your phone number has been saved.')
    else:
        print('Thank you for using the tire volume calculator.')
    # Append to the end of the volumes.txt file one line of text that contains the five values
    print(f'{current_date:%Y-%m-%d}, {w}, {a}, {d}, {v:.2f}, {phone_number}', file=volumes_file)
    
print(f'\nThe approximate volume of the tire is {v:.2f} liters.')

