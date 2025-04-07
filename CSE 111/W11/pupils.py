import csv

# Each row in the pupils.csv file contains three elements.
# These are the indexes of the elements in each row.
GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
BIRTHDATE_INDEX = 2

def main():
    # Call the read_compound_list function to read the contents of the pupils.csv file.
    students_list = read_compound_list("pupils.csv")
    # Write a lambda function that will extract the birthdate from a student.
    # birthdate = lambda student: student[BIRTHDATE_INDEX]
    # Write a call to the Python built-in sorted function that will sort the students_list by birthdate from oldest to youngest.
    # sorted_students = sorted(students_list, key=birthdate)
    # Print the students_list by calling the print_list function.
    # print_list(sorted_students)

    # STRETCH 1:
    # Write a lambda function that will extract the given name from a student.
    # given_name = lambda student: student[GIVEN_NAME_INDEX]
    # Write a call to the Python built-in sorted function that will sort the students_list by given name from A to Z.
    # sorted_students = sorted(students_list, key=given_name)
    # Print the students_list by calling the print_list function.
    # print_list(sorted_students)

    # STRETCH 2:
    # Write a lambda function that will extract the birthdate and month from a student with a substring and ignoring the year.
    birthday = lambda student: student[BIRTHDATE_INDEX][5:]
    # Write a call to the Python built-in sorted function that will sort the students_list by birthdate and month from January to December.
    sorted_students = sorted(students_list, key=birthday)
    # Print the students_list by calling the print_list function.
    print_list(sorted_students)

def read_compound_list(filename):
    """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.

    Parameter
        filename: the name of the CSV file to read.
    Return: the compound list
    """
    # Create an empty list.
    compound_list = []

    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            # Append the current row at the end of the compound list.
            compound_list.append(row)

    return compound_list

def print_list(data_list):
    # Print the contents of the compound list.
    for row in data_list:
        print(data_list)

# At the bottom of the pupils.py file write a call to the main function.
if __name__ == "__main__":
    main()
