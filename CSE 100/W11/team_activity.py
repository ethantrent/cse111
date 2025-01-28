# Have your program open the HR System file, read through it line by line, and at this point, simply display the line to the screen.

# Split the line into parts and change your display, so that it shows only the names (instead of the whole line).

# For each line, get the name and the job title for each person, and display those to the screen.

with open("hr_system.txt") as f:
    # The file has now been opened and stored in a variable "f"

    # Read each line, one by one, into a variable: current_line
    for line in f:
        # Strip off leading/trailing whitespace
        # Split the current line into its parts based on a space " " as the separator
        clean_line = line.strip()
        parts = clean_line.split(" ")

        # Save the parts we need into variables
        name = parts[0]
        id = parts[1]
        title = parts[2]
        salary = parts[3]

        # Output the name and title as desired
        print(f"Name: {name}, ID: {id}, Title: {title} - Salary: ${salary:.2f}")