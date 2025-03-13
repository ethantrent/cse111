"""Open the students.csv file for reading, skip the first line of text in the file because it contains only headings, 
and read the other lines of the file into a dictionary. The program must store each student I-Number as a key and each 
I-Number name pair or each name as a value in the dictionary.

Get an I-Number from the user, use the I-Number to find the corresponding student name in the dictionary, and print the name.
If a user enters an I-Number that doesn't exist in the dictionary, your program must print the message, 
"No such student" (without the quotes)."""

import csv

def main():
    # Constants for the columns in the CSV file
    I_NUMBER_INDEX = 0
    NAME_INDEX = 1
    # Read the student data from the CSV file
    students_dict = read_dictionary("students.csv", I_NUMBER_INDEX)
    # Get an I-Number from the user
    inumber = input("Enter an I-Number (xx-xxx-xxxx): ")
    # The I-Numbers are stored in the CSV file as digits only (without
    # any dashes), so we remove all dashes from the user's input.
    inumber = inumber.replace("-", "")
    # Determine if the user input is formatted correctly.
    if not inumber.isdigit():
        print("Invalid character in I-Number")
    else:
        if len(inumber) < 9:
            print("Invalid I-Number: too few digits")
        elif len(inumber) > 9:
            print("Invalid I-Number: too many digits")
        else:
            # The user input is a valid I-Number. Find
            # the I-Number in the list of I-Numbers.
            if inumber not in students_dict:
                print("No such student")
            else:
                # Retrieve the student name that corresponds
                # to the I-Number that the user entered.
                value = students_dict[inumber]
                name = value[NAME_INDEX]

                # Print the student name.
                print(name)

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
    Return: a dictionary that contains
        the contents of the CSV file.
    """
    # Create an empty dictionary that will
    # store the data from the CSV file.
    dictionary = {}
    # open the CSV file for reading
    with open(filename, "rt") as file:
        # create a csv reader object
        csv_reader = csv.reader(file)
        # skip the first row of the csv file
        next(csv_reader)
        # create a dictionary to store the student data
        students_dict = {}
        # iterate through each row in the csv file
        for line in csv_reader:
            # From the current row, retrieve the data
            # from the column that contains the key.
            key = line[key_column_index]
            # Store the data from the current row
            # into the dictionary.
            dictionary[key] = line
    # Return the dictionary that contains the data
    return dictionary

if __name__ == "__main__":
    main()