# USER DEFINED FUNCTIONS
# A user-defined function is written by a programmer like yourself as part of a program
# Writing user-defined functions has several advantages, including:
# making your code more reusable
# making your code easier to understand and debug
# making your code easier to change and add capabilities

# HOW TO WRITE A USER DEFINED FUNCTION
# To write a user-defined function in Python, simply type code that matches this template:

"""
def function_name(param1, param2, … paramN):
    documentation string
    statement1
    statement2
        ⋮
    statementN
    return value
"""

# The first line of a function is called the header or signature, and it includes the following:
# the keyword def (which is an abbreviation for "define")
# the function name
# the parameter list (with the parameters separated by commas)

# Here is the header for a function named draw_circle that takes three parameters named x, y, and radius:

# def draw_circle(x, y, radius):
# You could read the previous line of code as,
# "Define a function named draw_circle that takes three parameters named x, y, and radius.""

# # Example 1

import math

# Define a function named print_cylinder_volume.
def print_cylinder_volume():
    """Compute and print the volume of a cylinder.
    Parameters: none
    Return: nothing
    """
    # Get the radius and height from the user.
    radius = float(input("Enter the radius of a cylinder: "))
    height = float(input("Enter the height of a cylinder: "))

    # Compute the volume of the cylinder.
    volume = math.pi * radius**2 * height

    # Print the volume of the cylinder.
    print(f"Volume: {volume:.2f}")

# Because the print_cylinder_volume function in example 1 doesn’t accept parameters, 
# it must be called without any arguments like this:

    print_cylinder_volume()

# How to Make a User-Defined Function Reusable

# The most reusable functions are ones that take parameters, perform calculations, 
# and return a result but do not perform user input and output.

# Example 2

import math

# Define a function named print_cylinder_volume.
def print_cylinder_volume(radius, height):
    """Compute and print the volume of a cylinder.
    Parameters
        radius: the radius of the cylinder
        height: the height of the cylinder
    Return: nothing
    """
    # Compute the volume of the cylinder.
    volume = math.pi * radius**2 * height

    # Print the volume of the cylinder.
    print(volume)

# Because the second version of the print_cylinder_volume function accepts two parameters, 
# it must be called with two arguments like this:

    print_cylinder_volume(2.5, 4.1)
    
# To return a result from a function, simply type the keyword return followed by whatever result you want 
# returned to the calling function. Example 3 contains a third version of the cylinder volume function

# Example 3

import math

# Define a function named computer_cylinder_volume.
def compute_cylinder_volume(radius, height):
    """Compute and return the volume of a cylinder.
    Parameters
        radius: the radius of the cylinder
        height: the height of the cylinder
    Return: the volume of the cylinder
    """
    # Compute the volume of the cylinder.
    volume = math.pi * radius**2 * height

    # Return the volume of the cylinder so that the
    # volume can be used somewhere else in the program.
    return volume

# Many functions that you’ve used in the past such as input, float, and round, return a result. 
# When a function returns a result, we usually write code to store that returned result in 
# a variable to use later in the program like this:

    text = input("Please enter your name: ")

 #Because the compute_cylinder_volume function in example 3 accepts two parameters and returns a result, 
 # it could be called like this:

    volume = compute_cylinder_volume(2.5, 4.1)

# The main User-Defined Function

# Example 4

import math

# Get the radius and height from the user.
radius = float(input("Enter the radius of a cylinder: "))
height = float(input("Enter the height of a cylinder: "))

# Compute the volume of the cylinder.
volume = math.pi * radius**2 * height

# Print the volume of the cylinder.
print(f"Volume: {volume:.2f}")

# The code in example 4 is not a function. It is a program that computes the volume of a cylinder.
# Example 5 contains the same Python program as example 4 except most of the statements are inside a user-defined function named main.

# Example 5

import math

# Define a function named main.
def main():
    # Get the radius and height from the user.
    radius = float(input("Enter the radius of a cylinder: "))
    height = float(input("Enter the height of a cylinder: "))

    # Compute the volume of the cylinder.
    volume = math.pi * radius**2 * height

    # Print the volume of the cylinder.
    print(f"Volume: {volume:.2f}")

# Start this program by
# calling the main function.
main()

# Notice the call to the main function in example 5 at line 19. Without that call to the main function, 
# when we run the program, the program will do nothing

# A Complete Program with User-Defined Functions

# A better way to write the program in examples 1 and 5 is to separate the program into two functions, 
# one named main and one named compute_cylinder_volume as shown in example 6.

# Example 6

import math

# Define the main function.
def main():
    # Get a radius and a height from the user.
    radius = float(input("Enter the radius of a cylinder: "))
    height = float(input("Enter the height of a cylinder: "))

    # Call the compute_cylinder_volume function and store
    # its return value in a variable to use later.
    volume = compute_cylinder_volume(radius, height)

    # Print the volume of the cylinder.
    print(f"Volume: {volume:.2f}")


# Define a function that accepts two parameters.
def compute_cylinder_volume(radius, height):
    """Compute and print the volume of a cylinder.
    Parameters
        radius: the radius of the cylinder
        height: the height of the cylinder
    Return: the volume of the cylinder
    """
    # Compute the volume of the cylinder.
    volume = math.pi * radius**2 * height

    # Return the volume of the cylinder so that the
    # volume can be used somewhere else in the program.
    # The returned result will be available wherever
    # this function was called.
    return volume


# Start this program by
# calling the main function.
main()