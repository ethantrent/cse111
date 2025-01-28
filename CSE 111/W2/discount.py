"""
Work as a team to write a Python program named discount.py that gets a customer’s subtotal as input and gets the current day
of the week from your computer’s operating system. Your program must not ask the user to enter the day of the week. 
Instead, it must get the day of the week from your computer’s operating system.

If the subtotal is $50 or greater and today is Tuesday or Wednesday, your program must subtract 10% from the subtotal. 
Your program must then compute the total amount due by adding sales tax of 6% to the subtotal. 
Your program must print the discount amount if applicable, the sales tax amount, and the total amount due.
"""

# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

# Call the weekday() method to get the day of the
# week from the current_date_and_time object.
day_of_week = current_date_and_time.weekday()

# Ask the user for the subtotal of the customer's purchase.
subtotal = float(input('Please Enter The Subtotal: '))

# Check if the subtotal is $50 or greater and today is Tuesday or Wednesday.
if subtotal >= 50 and day_of_week in [1, 2]:
    # Calculate the discount amount by subtracting 10% from the subtotal.
    discount = subtotal * 0.10
    # Calculate the total amount due by adding sales tax of 6% to the subtotal.
    total = subtotal - discount + (subtotal * 0.06)
    # Print the discount amount, sales tax amount, and total amount due.
    print(f'\nDiscount Amount: ${discount:.2f}\n'
          f'Sales Tax Amount: ${subtotal * 0.06:.2f}\n'
          f'Total Amount Due: ${total:.2f}')
else:
    # Calculate the total amount due by adding sales tax of 6% to the subtotal.
    total = subtotal + (subtotal * 0.06)
    # Print the sales tax amount and total amount due.
    print(f'\nSales Tax Amount: ${subtotal * 0.06:.2f}\n'
          f'Total Amount Due: ${total:.2f}')