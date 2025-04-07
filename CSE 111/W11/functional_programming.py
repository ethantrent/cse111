# TYPES OF PROGRAMMING PARADIGMS

"""A paradigm is a way of thinking or a way of perceiving the world. There are at least four main paradigms for programming a computer: 
procedural, declarative, functional, and object-oriented."""

"""Procedural programming is a programming paradigm that focuses on the process or the steps to accomplish a task. 
This is the type of programming that you did in CSE 110 and in previous lessons of CSE 111."""

"""Declarative programming is a programming paradigm that does not focus on the process or steps to accomplish a task. 
Instead, with declarative programming, a programmer focuses on what she wants from the computer, or in other words, 
she focuses on the desired results. The SQL programming language is a good example of a declarative language. 
If you have ever written SQL code, then you have used declarative programming. When writing SQL code, a programmer writes 
code to tell the computer what she wants in the results but not the steps the computer must folFlow to get those results."""

"""Functional programming is a programming paradigm that focuses on functions and avoids shared state, mutating state, and side effects.
There are many techniques and concepts that are part of functional programming."""

# PASSING A FUNCTION INTO ANOTHER FUNCTION

"""The Python programming language allows a programmer to pass a function as an argument into another function. 
A function that accepts other functions in its parameters is known as a higher-order function. 
Higher-order functions are often used to process the elements in a list."""

# Example 1

def main():
    fahr_temps = [72, 65, 71, 75, 82, 87, 68]

    # Print the Fahrenheit temperatures.
    print(f"Fahrenheit: {fahr_temps}")

    # Convert each Fahrenheit temperature to Celsius and store
    # the Celsius temperatures in a list named cels_temps.
    cels_temps = []
    for fahr in fahr_temps:
        cels = cels_from_fahr(fahr)
        cels_temps.append(cels)

    # Print the Celsius temperatures.
    print(f"Celsius: {cels_temps}")


def cels_from_fahr(fahr):
    """Convert a Fahrenheit temperature to
    Celsius and return the Celsius temperature.
    """
    cels = (fahr - 32) * 5 / 9
    return round(cels, 1)


# Call main to start this program.
if __name__ == "__main__":
    main()

"""there is a for loop that converts each Fahrenheit temperature to Celsius and then appends the Celsius temperature onto a new list. 
Writing a for loop like this is the traditional way to process all the elements in a list and doesn't use higher-order functions."""

# Example 2

def main():
    fahr_temps = [72, 65, 71, 75, 82, 87, 68]

    # Print the Fahrenheit temperatures.
    print(f"Fahrenheit: {fahr_temps}")

    # Convert each Fahrenheit temperature to Celsius and store
    # the Celsius temperatures in a list named cels_temps.
    cels_temps = list(map(cels_from_fahr, fahr_temps)) # the map function has a loop inside it and doesn’t have to write the loop
    # the first argument to the map function is the name of the cels_from_fahr function. we are passing the cels_from_fahr function 
    # into the map function, so that map will call cels_from_fahr for each element in the fahr_temps list.

    # Print the Celsius temperatures.
    print(f"Celsius: {cels_temps}")


def cels_from_fahr(fahr):
    """Convert a Fahrenheit temperature to
    Celsius and return the Celsius temperature.
    """
    cels = (fahr - 32) * 5 / 9
    return round(cels, 1)


# Call main to start this program.
if __name__ == "__main__":
    main()

"""Python includes a built-in higher-order function named map that will process all the elements in a list and return a new list 
that contains the results. The map function accepts a function and a list as arguments and contains a loop inside it, so that when 
a programmer calls the map function, he doesn't need to write a loop. The map function is a higher-order function because it accepts 
a function as an argument."""

# NESTED FUNCTIONS

"""The Python programming language allows a programmer to define nested functions. A nested function is a function that is defined 
inside another function and is useful when we wish to split a large function into smaller functions and the smaller functions 
will be called by the containing function only"""

# Example 3

def main():

    def cels_from_fahr(fahr): # nested function
        """Convert a Fahrenheit temperature to
        Celsius and return the Celsius temperature.
        """
        cels = (fahr - 32) * 5 / 9
        return round(cels, 1)

    fahr_temps = [72, 65, 71, 75, 82, 87, 68]

    # Print the Fahrenheit temperatures.
    print(f"Fahrenheit: {fahr_temps}")

    # Convert each Fahrenheit temperature to Celsius and store
    # the Celsius temperatures in a list named cels_temps.
    cels_temps = list(map(cels_from_fahr, fahr_temps))

    # Print the Celsius temperatures.
    print(f"Celsius: {cels_temps}")


# Call main to start this program.
if __name__ == "__main__":
    main()

"""In this example, the cels_from_fahr function is defined inside the main function. The cels_from_fahr function is a nested function"""

# LAMBDA FUNCTIONS

"""A Python lambda function is a small anonymous function, meaning a small function without a name. A lambda function is always a 
small function because the Python language restricts a lambda function to just one expression."""

# Example 4

def main():
    fahr_temps = [72, 65, 71, 75, 82, 87, 68]

    # Print the Fahrenheit temperatures.
    print(f"Fahrenheit: {fahr_temps}")

    # Define a lambda function that converts
    # a Fahrenheit temperature to Celsius and
    # returns the Celsius temperature.
    cels_from_fahr = lambda fahr: round((fahr - 32) * 5 / 9, 1)

    # Convert each Fahrenheit temperature to Celsius and store
    # the Celsius temperatures in a list named cels_temps.
    cels_temps = list(map(cels_from_fahr, fahr_temps))

    # Print the Celsius temperatures.
    print(f"Celsius: {cels_temps}")


# Call main to start this program.
if __name__ == "__main__":
    main()

"""cels_from_fahr is the name of a variable, not the name of the lambda function. The lambda function has no name."""

"""Notice in the next example that the lambda function is defined inside the parentheses for the call to the map function."""

    # Convert each Fahrenheit temperature to Celsius and store
    # the Celsius temperatures in a list named cels_temps.
fahr_temps = [72, 65, 71, 75, 82, 87, 68]
cels_temps = list(map(
        lambda fahr: round((fahr - 32) * 5 / 9, 1),
        fahr_temps))
"""    lambda param1, param2, … paramN: expression""" # parameters separated by commas, then a colon (:), and finally an 
# expression that performs arithmetic, modifies a string, or computes something else.

# MAP AND FILTER

# Example 5

def main():
    # Read a file that contains a list
    # of Canadian province names.
    provinces_list = read_list("provinces.txt")

    # As a debugging aid, print the entire list.
    print("Original list of provinces:")
    print(provinces_list)
    print()

    # Define a nested function that converts AB to Alberta.
    def alberta_from_ab(province_name):
        if province_name == "AB":
            province_name = "Alberta"
        return province_name

    # Replace all occurrences of "AB" with "Alberta" by
    # calling the map function and passing the ablerta_from_ab
    # function and provinces_list into the map function.
    new_list = list(map(alberta_from_ab, provinces_list)) # the map function convert all elements that are "AB" to "Alberta."
    print("List of provinces after AB was changed to Alberta:")
    print(new_list)
    print()

    # Define a lambda function that returns True if a
    # province's name is Alberta and returns False otherwise.
    is_alberta = lambda name: name == "Alberta"

    # Filter the new list to only those provinces that
    # are "Alberta" by calling the filter function and
    # passing the is_alberta function and new_list.
    filtered_list = list(filter(is_alberta, new_list)) # the filter function removes all elements that are not "Alberta."
    print("List filtered to Alberta only:")
    print(filtered_list)
    print()

    # Because all the elements in filtered_list are
    # "Alberta", we can count how many elements are
    # "Alberta" by simply calling the len function.
    count = len(filtered_list) # Calling the len function to count the number of elements that remain in the filtered list.

    print(f"Alberta occurs {count} times in the modified list.")


# Call main to start this program.
if __name__ == "__main__":
    main()

# SORTING

"""Python includes a built-in higher-order function named sorted that accepts a list as an argument and returns a new sorted list. 
Calling the sorted function is straightforward for a simple list such as a list of strings or a list of number"""

# Example 6

def main():
    # Create a list that contains country names
    # and print the list.
    countries = [
        "Canada", "France", "Ghana", "Brazil", "Japan"
    ]
    print(countries)

    # Sort the list. Then print the sorted list.
    sorted_list = sorted(countries) # the sorted function returns a new list that is sorted in ascending order.
    print(sorted_list)


# Call main to start this program.
if __name__ == "__main__":
    main()

"""A compound list is a list that contains lists. Sorting a compound list is more complex than sorting a simple list."""

    # Create a list that contains data about countries.
countries = [
        # [country_name, land_area, population, gdp_per_capita]
        ["Mexico", 1972550, 126014024, 21362],
        ["France",  640679,  67399000, 45454],
        ["Ghana",   239567,  31072940,  7343],
        ["Brazil", 8515767, 210147125, 14563],
        ["Japan",   377975, 125480000, 41634]
    ]

"""Perhaps we want the countries compound list sorted by country name or perhaps we want it sorted by population. 
The element that we want a list sorted by is known as the key element. If we want to use the sorted function to sort a 
compound list, we must tell the sorted function which element is the key element, which we do by passing a small 
function as an argument into the sorted function. This small function is called the key function and extracts the key element """

# Example 7

def main():
    # Create a list that contains data about countries.
    countries = [
        # [country_name, land_area, population, gdp_per_capita]
        ["Mexico", 1972550, 126014024, 21362],
        ["France",  640679,  67399000, 45454],
        ["Ghana",   239567,  31072940,  7343],
        ["Brazil", 8515767, 210147125, 14563],
        ["Japan",   377975, 125480000, 41634]
    ]

    # Print the unsorted list.
    print("Original unsorted list of countries")
    for country in countries:
        print(country)
    print()

    # Define a lambda function that will be used as the
    # key function by the sorted function. The lambda
    # function extracts the population data from a
    # country so that the population will be used for
    # sorting the list of countries.
    POPULATION_INDEX = 2
    popul_func = lambda country: country[POPULATION_INDEX]

    # Sort the list of countries by the population.
    sorted_list = sorted(countries, key=popul_func)

    # Print the sorted list.
    print("List of countries sorted by population")
    for country in sorted_list:
        print(country)


# Call main to start this program.
if __name__ == "__main__":
    main()

"""By using a key function it's possible to sort a compound list with a key element that isn't in the list."""

# Example 8

def main():
    # Create a list that contains data about young students.
    students = [
        # [given_name, surname, reading_level]
        ["Robert", "Smith", 6.7],
        ["Annie", "Smith", 6.2],
        ["Robert", "Lopez", 7.1],
        ["Sean", "Li", 5.6],
        ["Sofia", "Lopez", 5.3],
        ["Lily", "Harris", 6.7],
        ["Alex", "Harris", 5.8]
    ]

    GIVEN_INDEX = 0
    SURNAME_INDEX = 1

    # Define a lambda function that combines
    # a student's surname and given name.
    combine_names = lambda student_list: \
        f"{student_list[SURNAME_INDEX]}, {student_list[GIVEN_INDEX]}" # the lambda function combines the surname and given name.

    # Sort the list by the combined key of surname, given_name.
    sorted_list = sorted(students, key=combine_names) # the sorted function sorts the list by the combined key of surname, given_name.

    # Print the list.
    for student in sorted_list:
        print(student)


# Call main to start this program.
if __name__ == "__main__":
    main()




