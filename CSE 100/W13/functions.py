# functions are used to repeat code that is used multiple times in a program

# define a function by using the def keyword
def your_function_name():
    # code here
    # for the
    # body of the function
    pass

# call the function by giving its name and including the parentheses afterward
# First define the function
def print_message():
    print("Hello CSE 110 World!")
# Call the function now
    print_message()
# Call it again here
    print_message()

# When you define a function, you can declare parameters, which are values that it receives from the place that called it
def print_double(value):
    double_value = value * 2
    print(double_value)
# Then, you can call this function and pass it any value
print_double(12) # outputs 24
print_double(3) # outputs 6
print_double(42) # outputs 84

# Extending the previous example, suppose you want to have the program calculate the double value and return it,
# instead of printing it to the screen, in case you want to use it in further calculations
def get_double(value):
    double_value = value * 2
    return double_value
# Now the value is given back to the code that called it
new_number = get_double(4)
# The variable new_number would now have the value 8

# you need to be aware that whether you use the same variable name or not, 
# the function will have it's own copy of the value. And you can't use it outside of the function.
def get_double(value):
    double_value = value * 2
    return double_value

new_number = get_double(4)

# ERROR: This does not work, because the variable "double_value" is only alive during
# the body of the function. Down here, we have chosen to give the return value the name "new_number"

# the same applies for parameters
def print_message(the_message):
    print(the_message)

# it works just fine to use the same variable name as the function did...
the_message = "Message 1"
print_message(the_message)

# but it also works to use a different variable...
user_message = "Message 2"
print_message(user_message)
# In either of the two cases above, when you are in the function, 
# you'll want to use the variable name the_message regardless of what it was called down below.

# Most often variables refer to things so it is most common to use nouns for them
# Functions on the other hand do things or perform actions, so it is more common to use verbs for their names