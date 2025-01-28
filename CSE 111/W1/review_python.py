# COMMENTS

# A comment in a computer program is a note or description that is supposed to help a programmer understand the program. 
# Computers ignore comments in a program. In Python, a comment begins with the hash symbol (#) 
# and extends to the end of the current line.

# This is a comment because it has
# hash symbols at the beginning.

# VARIABLES

# A variable is a location in a computer’s memory where a program stores a value. 
# A variable has a name, a data type, and a value. In Python, we assign a value to a variable 
# by using the assignment operator, which is the equals symbol (=). A computer may change the value 
# and data type of a variable while executing a program.

# Here are four Python variables.
length = 5
time = 7.2
in_flight = True
first_name = "Cho"

# DATA TYPES

# Python has many data types including str, bool, int, float, list, and dict.
# A str (string) is any text inside single or double quotes, any text that a user enters, and any text in a text file. For example:

# Here are two string variables.
greeting = "Hello"
text = "23"

# A bool (Boolean variable) is a variable that stores either True or False. A Boolean variable may not store any other value besides True or False. For example:
# Here is a Boolean variable.
found = True

# An int (integer) is a whole number like 14. An int may not have a fractional part or digits after the decimal point. For example:
# Here is a variable that stores an int.
x = 14

# A float (floating point number) is a number that may have a fractional part or digits after the decimal point like 7.51. For example:
# Here is a variable that stores a float.
sample = 7.51

# LIST

# A list is a collection of values. Each value in a list is called an element and is stored at a unique index. 
# The primary purpose of a list is to efficiently store many elements. In a Python program, 
# we can create a list by using square brackets ([ and ]) and separating the elements with commas (,). 
# For example here are two lists named colors and samples:

# Here are two varibles that each store a list.
colors = ["yellow", "red", "green", "yellow", "blue"]
samples = [6.5, 7.2, 7.0, 8.1, 7.2, 6.8, 6.8]

# A dict (dictionary) is a collection of items. Each item is a key value pair. 
# The primary purpose of a dictionary is to enable a computer to find items very quickly. 
# In a Python program, we can create a dictionary by using curly braces ({ and }) and separating the items with commas (,). 
# For example:

# Here is a Python variable that stores a dict.
students = {
    "42-039-4736": "Clint Huish",
    "61-315-0160": "Amelia Davis",
    "10-450-1203": "Ana Soares",
    "75-421-2310": "Abdul Ali",
    "07-103-5621": "Amelia Davis"
}

# It is possible to convert between many of the data types. For example, to convert from any data type to a string, 
# we use the str() function. To convert from a string to an integer, we use the int() function, 
# and to convert from a string to a float, we use the float() function. The int() and float() functions 
# are especially useful to convert user input, which is always a string, to a number. 

# USER INPUT

# In a Python program, we use the input() function to get input from a user in a terminal window. 
# The input function always returns a string of characters.

text = input("Please enter your name: ")
color = input("What is your favorite color? ")

# DISPLAY RULES

# In a Python program, we use the print() function to display results to a user. 
# The easiest way to print both text and numbers together is to use a formatted string literal (also known as an f-string).

rate = 72
print(f"Heart rate: {rate}")

# ARITHMETIC OPERATORS

# Python has many arithmetic operators including power (**), negation (-), multiplication (*), 
# division (/), floor division (//), modulo (%), addition (+), and subtraction (-).

# The modulo operator (%), sometimes called the modulus operator, causes a computer to calculate the remainder after division. 
# For example, the following Python code causes the computer to store 2 in the variable result. 
# The value in x is 17 and the value in y is 3. 17 % 3 causes the computer to divide 17 by 3. 17 divided by 3 is 5 with a remainder of 2.

x = 17
y = 3
result = x % y
print(result)

# When we write an arithmetic expression that contains more than one operator, the computer executes the operators according
# to their precedence, also known as the order of operations. 

# SHORTHAND OPERATORS

# The Python programming language includes many augmented assignment operators, also known as shorthand operators. 
# All the shorthand operators have the same precedence as the assignment operator (=). 
# Here is a list of some of the Python shorthand operators:

# **=  *=  /=  //=  %=  +=  -=

# IF STATEMENTS

# In Python, we use if statements to cause the computer to make decisions; if statements are also called selection statements 
# because the computer selects one group of statements to execute and skips the other group of statements.

# There are six comparison operators that we can use in an if statement:
# <	less than
# <= less than or equal
# >	greater than
# >= greater than or equal
# == equal to
# != not equal to

# ELIF STATEMENTS

# Each if statement may have an else statement
# We can combine else and if into the keyword elif

# Get the cost of an item from the user.
cost = float(input("Please enter the cost: "))

# Determine a discount rate based on the cost.
if cost < 100:
    rate = 0.10
elif cost < 250:
    rate = 0.15
elif cost < 400:
    rate = 0.18
else:
    rate = 0.20

# Compute the discount amount
# and the discounted cost.
discount = cost * rate
cost -= discount

# Print the discounted cost for the user to see.
print(f"After the discount, you will pay {cost:.2f}")

# LOGICAL OPERATORS

# Python includes two logic operators which are the keywords and, or that we can use to combine two comparisons. 
# Python also includes the logical not operator. Notice in Python that the logical operators are literally the words: 
# and, or, not and not symbols as in other programming languages:

driver = 16
passenger = 18

if driver >= 54 or (driver >= 32 and passenger >= 54):
    message = "Enjoy the ride!"

