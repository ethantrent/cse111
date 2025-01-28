# Variable Scope

# The scope of a variable determines how long that variable exists and where it can be used. 
# Within a Python program, there are two categories of scope: local and global. 
# A variable has local scope when it is defined (assigned a value) inside a function. 
# A variable has global scope when it is defined outside of all functions. 
# Here is a small Python program that has two variables: g and x. g is defined outside 
# of all functions and therefore has global scope. x is defined inside the main function and therefore has local scope.

# g is a global variable because it
# is defined outside of all functions.
g = 25

def main():
    # x is a local variable because
    # it is defined inside a function.
    x = 1


# Global variables are accessible from anywhere in a program.
nShapes = 0

def square_area(length):
    # Local variables are only accessible from within the function where they are defined.
    area = length * length
    return area

def rectangle_area(width, length):
    area = width * length
    return area

# Two variables with the same name can exist in the same program as long as they are in different scopes or functions.
# When you write a program, you should use local variables whenever possible and use global varibles only when absolutely necessary

# COMMON MISTAKES

# Example 3

import math

def main():
    radius = float(input("Enter the radius of a circle: "))
    area = circle_area()
    print(f"area: {area:.1f}")

def circle_area():
    # Mistake! There is no variable named radius
    # defined inside this function, so the variable
    # radius cannot be used in this function.
    # area = math.pi * radius * radius
    # return area
    pass

main()

# The correct way to fix the mistake is to add a parameter to the circle_area function

# Example 4

import math

def main():
    radius = float(input("Enter the radius of a circle: "))
    area = circle_area(radius)
    print(f"area: {area:.1f}")

def circle_area(radius):
    area = math.pi * radius * radius
    return area

main()


# Default Parameter Values and Optional Arguments

# Python allows function parameters to have default values. If a parameter has a default value, 
# then its corresponding argument is optional. If a function is called without an argument, the corresponding 
# parameter gets its default value.

# Example 5

import math

def main():
    # Call the arc_length function with only one argument
    # even though the arc_length function has two parameters.
    len1 = arc_length(4.7)
    print(f"len1: {len1:.1f}")

    # Call the arc_length function again but
    # this time with two arguments.
    len2 = arc_length(4.7, 270)
    print(f"len2: {len2:.1f}")


# Define a function with two parameters. The
# second parameter has a default value of 360.
def arc_length(radius, degrees=360):
    """Compute and return the length of an arc of a circle"""
    circumference = 2 * math.pi * radius
    length = circumference * degrees / 360
    return length


main()


# FUNCTION DESIGN

# When designing functions, you should follow these guidelines:
# A good function is understandable by other programmers
# A good function is reusable
# A good function performs a single task that the programmer can describe, and the function’s name matches its task
# A good function is relatively short, perhaps fewer than 20 lines of code
# A good function has as few decision points (if statements and loops) as possible