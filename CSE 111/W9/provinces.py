"""Write a Python program named provinces.py that reads the contents of provinces.txt into a list and then modifies the list. 
Your program must do the following:

Open the provinces.txt file for reading.
Read the contents of the file into a list where each line of text in the file is stored in a separate element in the list.
Print the entire list.
Remove the first element from the list.
Remove the last element from the list.
Replace all occurrences of "AB" in the list with "Alberta".
Count the number of elements that are "Alberta" and print that number.
Testing Procedure"""

def main():
    # Read the contents of a text file
    # named provinces.txt into a list.
    text_list = read_list("provinces.txt")

    # Remove the first element from the list.
    text_list.pop(0)

    # Remove the last element from the list.
    text_list.pop()

    # Replace all occurrences of "AB" in the list with "Alberta".
    for i in range(len(text_list)):
        if text_list[i] == "AB":
            text_list[i] = "Alberta"

    # Print the modified list.
    print(text_list)
    
    print()

    # Count the number of elements that are "Alberta" and print that number.
    count = text_list.count("Alberta")
    print(f"Alberta occurs {count} times in the list.")


def read_list(provinces):
    """Read the contents of a text file into a list and
    return the list. Each element in the list will contain
    one line of text from the text file.
    Return: a list of strings
    """
    # Create an empty list that will store
    # the lines of text from the text file.
    text_list = []

    # Open the text file for reading and store a reference
    # to the opened file in a variable named text_file.
    with open("provinces.txt", "rt") as text_file:

        # Read the contents of the text
        # file one line at a time.
        for line in text_file:

            # Remove white space, if there is any,
            # from the beginning and end of the line.
            clean_line = line.strip()

            # Append the clean line of text
            # onto the end of the list.
            text_list.append(clean_line)

    # Return the list that contains the lines of text.
    return text_list

# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()

