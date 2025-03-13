def main():
    # Write a list of strings to a text file
    data_list = ["Hello", "World", "Python", "Programming"]
    # Write the list to a text file
    write_text_file(data_list, "joy.txt")
    # Read
    file_data = read_text_file("joy.txt")
    # Print the data
    print(file_data)


def write_text_file(data_list, filename):
    # Open the file for writing
    with open(filename, "wt") as file:
        # Write each string in the list to the file
        for line in data_list:
            # Write a newline character
            print(line, file=file)


def read_text_file(filename):
    data_list = []
    # Open the file for reading
    with open(filename, "rt") as file:
        # Read all the lines from the file
        for line in file:
            # Remove the newline character
            line = line.strip()
            data_list.append(line)
    # Add the line to the list
    return data_list


if __name__ == "__main__":
    main()