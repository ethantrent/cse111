"""
Use all or any part of this file as a demonstration of dictionaries
during class in your section of CSE 111.

You could retain the numbered comments and delete all or any parts of
the code. Then give the modified file to your students and ask them to
write the code for the numbered comments. Or you could write the code
for the numbered comments with them as a demonstration during class.

Copyright 2020, Brigham Young University - Idaho. All rights reserved.
"""

import csv

def main():
    # 1. Create a dictionary with four key value pairs.
    clothing = {
        "75120" : "Jacket",
        "42133" : "Shirt",
        "10315" : "Socks",
        "10316" : "Socks"
    }

    # 2. Print the entire dictionary.
    print(clothing)
    print()

    # 3. Create an empty dictionary named tools.
    tools = {}

    # 4. Put one tool into the empty dictionary.
    tools["p135"] = "whisk"


    # 5. Put another tool into the tools dictionary.
    tools["p320"] = "spatula"

    # 6. Prompt the user to enter three more cooking
    # tools and put those in the tools dictionary.
    print("Please enter the tool number and name for three cooking tools.")
    for _ in range(3):
        tool_number = input("Enter the tool number: ")
        tool_name = input("Enter the tool name: ")
        tools[tool_number] = tool_name

    # 7. Print the entire tools dictionary.
    print(tools)
    print()

    # 8. Print just the keys from the tools dictionary.
    print(tools.keys())

    # 9. Print just the values from the tools dictionary.
    print(tools.values())

    # 10. Print the key value pairs as items from the tools dictionary.
    print(tools.items()) # this prints the key value pairs as tuples
    print()

    # 11. Print the items in the tools dictionary, one at a time.
    for key, value in tools.items():
        print(key, value) # unpacks the tuple into key and value

    # Although printing a dictionary is interesting, the real reason
    # to create a dictionary is to use the keys to find values.
    # Dictionaries are very fast at finding things.

    # 12. Prompt the user to enter a tool key. Lookup
    # and then print the corresponding tool name.
    key = input("Enter a tool's number: ")

    if key in tools:
        # Here it is! This is how to lookup something in a
        # dictionary. Many students miss this point. This is how
        # to do it. It's simple. value = dictionary_name[key]
        value = tools[key]
        print(f"Tool number {key} is {value}.")
    else:
        print(f"Tool number {key} doesn't exist")
    print()

    # 13. Write the tools dictionary to a csv file.
    print("Writing the tools dictionary to a csv file.")
    with open("tools.csv", "wt") as file: #wt means write text
        print("Tool Number, Tool Name", file=file) # prints the header to the file
        for key, value in tools.items():
            print(f"{key}, {value}", file=file) # file=file writes to the file

    # 14. Read the tools.csv file into a new dictionary.
    print("Reading the csv file into a new dictionary.")
    products_dict = {}
    with open("tools.csv", "rt") as file: #rt means read text
        next(file) # skip the header
        for line in file:
            parts_list = line.split(", ")
            key = parts_list[0].strip()
            value = parts_list[1].strip()
            products_dict[key] = value

    print(products_dict)
    print()

    # 15. Use the csv module to read the
    # tools.csv file into a new dictionary.
    print("Reading the csv file into another new dictionary.")
    # import csv is at the top of the file
    products_dict = {}
    with open("tools.csv", "rt") as file:
        csv_reader = csv.reader(file) # creates a csv reader object to read the file
        next(csv_reader)
        for key, value in csv_reader:
            products_dict[key] = value

    print(products_dict)
    print()

    # 16. Use a dictionary to count how many
    # cars were made by each manufacturer.
    cars_data = [
        ["1HGCM82633A123456", "Honda", 2019, "Red"],
        ["1FMDU32P9TZ123456", "Ford", 2018, "Blue"],
        ["1FMEU7DE2HUA12345", "Ford", 2021, "Black"],
        ["JTDKB20U693123456", "Toyota", 2020, "White"],
        ["2HGFB2F52EH123456", "Honda", 2021, "Silver"],
        ["1FM5K7F89DGA12345", "Ford", 2017, "Silver"],
        ["1G1ZT52825F123456", "Chevrolet", 2016, "Green"]
    ]

    manufacturer_counters = {}
    for car in cars_data:
            # The manufacturer is not yet in the dictionary. This
            # means the current car is the first car in the cars_data
            # list made by the current car's manufacturer. Therefore,
            # we start the counter for that manufacturer at 1.


            # Get the current count from the dictionary
            # and add one to that count.

        # Store the count into the dictionary with the manufacturer
        # name as the key and the count as the value.
        pass


if __name__ == "__main__":
    main()
