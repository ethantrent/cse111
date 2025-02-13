# Loops are REPITIONS

def main ():
    # Write a loop that prints the integers
    # between zero and 10, inclusive.

    for i in range(11): # use range(11) to include 10 since 0 is the first number
    # read as for each i in the range of 0 to 10
        print(i, end=", ") # i represents integer and end=", " is used to separate the integers by a comma and a space 
                           # to put on the same line

    """Another way to write the loop is:
    for i in range(0, 11): # 0 is the starting number and 10 is the ending number excluding 11
        print(i)

        OR

    i = 0
    while i <= 10:
        print(i)
        i += 1
    """

    print()

    # Write a loops that prints the integers
    # between three and ten, inclusive.

    for i in range (3, 11):
        print(i, end=", ")

    print()

    # Write a loop that prints the integers
    # 20, 25, 30, 35

    for i in range(20, 36, 5): # the third argument is the step value
        print(i, end=", ")

    """ i = 20
    while i <= 35:
        print(i)
        i += 5
    """
    print()

    # Write a loop that prints the integers
    # 40, 38, 36, 34, 32, 30

    for i in range(40, 28, -2):
        print(i, end=", ")
    
    """ i = 40
    while i >= 30:
        print(i)
        i -= 2
    """
    print()

    # Write a loop that stores the integers from
    # 0 to 10 in a list.

    numbers = [] # create an empty list
    for i in range(11):
        numbers.append(i) # add the integers to the list
    print(numbers)

    """i = 0
    while i <= 10:
    numbers.append(i)
    i += 1
    """
    print()

    # Write a loop that prints each element in the list
    # on a different line
    names = ["Alice", "Bob", "Charlie", "David", "Eve"]
    for name in names:
        print(name)

main()