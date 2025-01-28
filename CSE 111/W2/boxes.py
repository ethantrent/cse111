"""
A manufacturing company needs a program that will help its employees pack manufactured items into boxes for shipping. 
Write a Python program named boxes.py that asks the user for two integers:

1. the number of manufactured items
2. the number of items that the user will pack per box
Your program must compute and print the number of boxes necessary to hold the items. 
This must be a whole number. Note that the last box may be packed with fewer items than the other boxes.
"""

# Import math to call the ceil function
import math

# Ask the user for the number of manufactured items and the number of items per box
items = int(input('Please Enter The Number Of Manufactured Items: '))
per_box = int(input('Please Enter The Number Of Items Per Box: '))

# Calculate the number of boxes necessary to hold the items using the ceil function
boxes = math.ceil(items / per_box)

# Print for the user the number of boxes necessary to hold the items
print(f'\nFor {items} items, packing {per_box} items in each box'
      f', you will need {boxes} boxes.')

# 6 Function Calls (2 input, 2 int, 1 ceil, 1 print)

