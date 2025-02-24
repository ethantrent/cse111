"""
Use all or any part of this file as a demonstration of iteration (loops)
and lists during class in your section of CSE 111.

You could retain the numbered comments and delete all or any parts of
the code. Then give the modified file to your students and ask them to
write the code for the numbered comments. Or you could write the code
for the numbered comments with them as a demonstration during class.
"""

def main():
    # 1. Write a loop that prints the integers
    # between zero and ten, including zero and ten.
    i = 0
    while i <= 10:
        print(i, end=", ")
        i += 1
    print()
    for i in range(11):
        print(i, end=", ")
    print()

    # 2. Write a loop that prints the integers
    # between three and ten, including three and ten.
    i = 3
    while i <= 10:
        print(i, end=", ")
        i += 1
    print()
    for i in range(3, 11):
        print(i, end=", ")
    print()

    # 3. Write a loop that prints the integers 20, 25, 30, 35.
    for i in range(20, 36, 5):
        print(i, end=", ")
    print()
    i = 20
    while i <= 35:
        print(i, end=", ")
        i += 5
    print()

    # 4. Write a loop that prints the integers 40, 38, 36, 34, 32, 30.
    for i in range(40, 29, -2):
        print(i, end=", ")
    print()
    i = 40
    while i > 28:
        print(i, end=", ")
        i -= 2
    print()

    # 5. Write a loop that stores the integers from
    # zero to ten in a list. Include zero and ten.
    numbers = []
    for i in range(11):
        numbers.append(i)
    print(numbers)

    # 6. Write a loop that prints each element in a list on a different line. () is a tuple NOT a list
    people = ["James", "Lisa", "Juan", "Sophia", "William", "Noah", "Olivia"]
    for person in people:
        print(person)

    print()

    for i in range(len(people)):
        name = people[i]
        print(i, name) # prints index and name

    print()

    for i, name in enumerate(people):
        print(i, name) # prints index and name

    # Print a blank line.
    print()

    # 7. Below are two parallel lists. Write a loop that prints the elements
    # of both lists to a terminal window on separate lines like this:
    # Ashton 97
    # Chester 75
    # Drummond 83
    # Felt 72
    # Island Park 154
    # Wayan 78
    cities = ["Ashton", "Chester", "Drummond", "Felt", "Island Park", "Wayan"]
    snowfall = [97, 75, 83, 72, 154, 78]  # inches

    for i in range(len(cities)):
        print(cities[i], snowfall[i])
        #OR
        #city = cities[i]
        #inches = snowfall[i]
        #print(city, inches)
    # Print a blank line.
    print()

    print(list(zip(cities, snowfall))) # zip creates a list of tuples from two lists
    for city, inches in zip(cities, snowfall):
        print(city, inches) #prints each tuple on a separate line and unpacks the tuple

if __name__ == "__main__":
    main()
