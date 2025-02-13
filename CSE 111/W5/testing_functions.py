# TESTING FUNCTIONS
"""A much better way to test a program is to test its functions individually and to 
write separate test functions that automatically verify that the program’s functions are correct."""

# ASSERT STATEMENTS

"""In a computer program, an assertion is a statement that causes the computer to check if a comparison is true. 
When the computer checks the comparison, if the comparison is true, the computer will continue to execute the code
in the program. However, if the comparison is false, the computer will raise an AssertionError, which will 
likely cause the program to terminate."""

"""Imagine a program used by a bank to track account balances, deposits, and withdrawals. A programmer might write 
the first few lines of the deposit function like this:"""

def deposit(amount):
    # In order for this program to work correctly and
    # for the bank records to be correct, we must not
    # allow someone to deposit a zero or negative amount.
    assert amount > 0

"""Examples of other assertions that could be used"""

 #   assert temperature < 0
 #   assert len(given_name) > 0
 #   assert balance == 0
 #   assert school_year != "senior"

 # PYTEST

"""a third-party Python module that makes it easy to write and run test functions. 
pytest allows a programmer to write simple test functions. The name of each test function
should begin with "test_", and each test function should use the Python assert statement
to verify that a program function returns a correct result. """

# Example
def test_min():
    assert min(7, -3, 0, 2) == -3

# COMPARING FLOATING POINT NUMBERS

"""Because computers approximate floating-point numbers, we must carefully compare them in our 
test functions. It is a bad practice to check if floating-point numbers are equal using just 
the equality operator (==). A better way to compare two floating-point numbers is to subtract 
them and check if their difference is small"""

# Example 4

    # The variables e and f can be any floating-
    # point numbers from any calculation.
e = 7.135
f = 7.128
# The tolerance is the maximum difference between two floating-point numbers that 
# the programmer will allow and still consider the numbers to be equal.

if abs(e - f) < 0.01:
    print(f"{e} and {f} are close enough so")
    print("we'll consider them to be equal.")
else:
    print(f"{e} and {f} are not close and")
    print("therefor not equal.")

# APPROX FUNCTION

"""The approx function* compares two floating-point numbers and returns True if they are equal 
within an appropriate tolerance. Because the last three have default values, when we call approx,
we're not required to pass arguments for the last three parameters."""

def approx(expected_value, rel=None, abs=None, nan_ok=False):
    pass

# If we call approx with just one argument, approx will compare the actual value and expected value and 
# return True if the difference between the two values is less than one millionth of the expected value.

def test_function():
    assert actual_value == approx(expected_value)

# The approx function has two parameters, rel and abs, that we can use to give approx a better tolerance to use in its comparison. 

# Example 5
import math

def test_sqrt():
    assert math.sqrt(5) == approx(2.24, rel=0.01)

# The rel named argument causes the approx function to compute the tolerance relative to the expected value. 
# This means that the assert statement and the approx function in the previous example cause the computer to 
# verify that the actual value returned from math.sqrt(5) is within 1% (0.01) of 2.24.

# Example 6

    # Compute the tolerance.
    tolerance = expected_value * rel

    # Use the tolerance to determine if the actual
    # and expected values are close enough to be
    # considered equal.
    if abs(actual_value - expected_value) < tolerance:
        return True
    else:
        return False
    
# we learn that approx will return True if the difference between the actual value returned
# from math.sqrt(5) and the expected value is less than 0.0224 (2.24 * 0.01).
# We can also use the abs named argument to give approx a tolerance

# Example 7

def test_sqrt():
    assert math.sqrt(5) == approx(2.24, abs=0.01)

# This is different from the rel named argument which causes approx to return True if the difference is less than
# rel * expected_value. The abs named argument is simpler and easier to understand than the rel named argument.

# HOW TO TEST A FUNCTION

""" 1. Write a function that is part of your normal Python program.

2. Think about different parameter values that will cause the computer to execute all
the code in your function and will possibly cause your function to fail or return an incorrect result.

3. In a separate Python file, write a test function that calls your program function and uses an assert statement
to automatically verify that the value returned from your program function is correct.

4. Use pytest to run the test function.

5. Read the output of pytest and use that output to help you find and fix mistakes in both your program function and test function."""

# Example

# weather.py

def cels_from_fahr(fahr):
    """Convert a temperature in Fahrenheit to
    Celsius and return the Celsius temperature.
    """
    cels = (fahr - 32) * 5 / 9
    return cels

# To adequately test this function, we should call it at least three times with the following arguments.

# a negative number
# zero
# a positive number

# In a separate file named test_weather.py we write a test function named test_cels_from_fahr as follows:

# test_weather.py

from weather import cels_from_fahr
from pytest import approx
import pytest

def test_cels_from_fahr():
    """Test the cels_from_fahr function by calling it and
    comparing the values it returns to the expected values.
    Notice this test function uses pytest.approx to compare
    floating-point numbers.
    """
    assert cels_from_fahr(-25) == approx(-31.66667)
    assert cels_from_fahr(0) == approx(-17.77778)
    assert cels_from_fahr(32) == approx(0)
    assert cels_from_fahr(70) == approx(21.1111)

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])

# SEPARATING PROGRAM CODE FROM TEST CODE

"""It is a good idea to separate test functions and program functions because the separation 
makes it easy to release a program to users. One consequence of writing program functions and 
test functions in separate files is that we must add an import statement at the top of the test 
file that imports all the program functions that will be tested."""

from file_name import function_1, function_2, … function_N

# Instead of writing the following code to start our program running:

# Start this program by
# calling the main function.
main()

# We write an if statement above the call to main() like this:

# If this file is executed like this:
# > python program.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()

# WHICH PROGRAM FUNCTIONS SHOULD WE TEST?

"""we would like to write at least one test function for each program function. 
However, this may not always be possible. The easiest program functions to test 
are the functions that have parameters and return a value. The hardest program functions
to test are the functions that get user input, print results to a terminal window, or draw something to a window."""




