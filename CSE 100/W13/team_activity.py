# Write a function compute_area_square that accepts a single value as a parameter, and then computes the area and returns it.

# Below the function, write code to prompt the user for the side of a square and save it into a variable, 

# then pass this variable to the function to compute the area. Finally, get the result back from the function and display it.

# Repeat the previous step to write and test the functions compute_area_rectangle and compute_area_circle.

# Write a loop to ask the user what kind of shape they have, then prompt for the length of a side, or sides, or radius, 

# and then calls the appropriate function, and displays the result. The program should continue looping 

# until the user enters "quit" for the shape.

def compute_area_square(side):
    return side**2

def compute_area_rectangle(length, width):
    return length * width

def compute_area_circle(radius):
    return 3.14 * (radius**2)

while True:
    shape = input("What shape do you have? ").lower()
    if shape == "square":
        side = float(input("What is the length of a side of the square? "))
        print(f'The area of the square is: {compute_area_square(side)}')
    elif shape == "rectangle":
        length = float(input("What is the length of the rectangle? "))
        width = float(input("What is the width of the rectangle? "))
        print(f'The area of the rectangle is {compute_area_rectangle(length, width)}')
    elif shape == "circle":
        radius = float(input("What is the radius of the circle? "))
        print(f'The area of the circle is {compute_area_circle(radius)}')
    elif shape == "quit":
        break
    else:
        print("Invalid shape")