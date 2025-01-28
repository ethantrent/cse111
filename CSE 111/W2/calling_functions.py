# What is a Function?
# A function is a group of statements (computer commands) that together perform one task
# Python includes many built-in functions such as: input, int, float, str, len, range, abs, round, list, dict, open, and print
# A programmer uses a function by calling it (also known as invoking it). 

# Calling Functions
# To call (or invoke) a function means to write code that causes the computer to execute the code that is inside that function.

name = input("Please enter your name: ") # calling the input function
print(f"Hello {name}") # calling the print function

# A parameter is a piece of data that a function needs in order to complete its task
# An argument is the value that is passed through a parameter into a function. 
# In other words, parameters are listed in a function’s documentation, and arguments are listed in a call to a function.
# For example, the following code calls the built-in input function 
# and passes the string "Please enter your name: " as the argument for the prompt parameter.
# When a function has more than one parameter and a programmer writes code to call that function,
# the programmer nearly always writes the arguments in the same order as the parameters.

n = float(input("Please enter a number: ")) # calling the input function
r = round(n, 2) # calling the round function with first argument n and second argument 2
print(r) # calling the print function

# Optional Arguments
# When calling a function or method, some arguments are optional
n = float(input("Please enter a number: "))
r = round(n) # the round function will round the number in its first parameter to an integer
print(r)

# Named Arguments
# For some optional arguments, we must pass a named argument, 
# which is an argument that is preceded by the name of its matching parameter

x = "sun"
y = "moon"
z = "stars"
print(x, y, z, sep="|", flush=True)

# How to Call a Function that Is inside a Module
# A Python module is a collection of related functions. 
# The Python standard library includes many modules which have more functions, 
# such as the math module—which includes the floor, ceil, and sqrt functions and the random module—which 
# includes the randint, choice, and shuffle functions

import math # importing the math module

r = math.sqrt(71) # name of the function is math.sqrt and accepts one argumemt in the parameter (71)
print(r)

# How to Call a Method
# A method is a function that belongs to a class or object
# A method is a kind of function, so calling a method is similar to calling a function. 
# The difference is that to call a method we must type the name of the object and a period (.) in front of the method name

# Get a string of text from the user.
text1 = input("Enter a motivational quote: ")

# Call the built-in len function to get
# the number of characters in the text.
length = len(text1) # calls the built-in len function

# Call the string upper method to convert
# the quote to upper case characters.
text2 = text1.upper() # calls the string upper method

# Call the built-in print function to print
# the length of the text and the text in all
# upper case for the user to see.
print(length, text2)

# How to Store a Returned Value
# All the previous examples in this preparation content use the assignment operator (=) 
# to store the value returned from a function in a variable.
import math

# Get a number from the user.
number = float(input("Enter a number: "))

# Call the math.sqrt function and
# immediately print its return value.
print( math.sqrt(number) )

# Call the math.sqrt function again and
# use its return value in an if statement.
if math.sqrt(number) < 100:
    print(f"The square root is less than 100.")
elif math.sqrt(number) > 100:
    print(f"The square root is more than 100.")
else:
    print(f"The square root is exactly 100.")

# However, it is more common to store the return value in a variable so that it can be used multiple times.
import math

# Get a number from the user.
number = float(input("Enter a number: "))

# Call the math.sqrt function and store its
# return value in a variable to use later.
root = math.sqrt(number)

print(f"The square root is {root:.2f}")

if root < 100:
    print(f"The square root is less than 100.")
elif root > 100:
    print(f"The square root is more than 100.")
else:
    print(f"The square root is exactly 100.")


x = 3
y = 15
print(x, y, "Hello", sep=", ", end="; ")
print("Today is a great day!")