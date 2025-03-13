import csv
from datetime import datetime  # Import the datetime class from the datetime module so that it can be used in this program.

def main():
    try:
        # Call the read_dictionary function and store the compound dictionary in a variable named products_dict.
        products_dict = read_dictionary("products.csv", 0)
        # Print the store name.
        print("Groceries R Us:")
        print()
        # Open the request.csv file for reading.
        with open("request.csv", "r") as file:
            # Create a CSV reader object.
            reader = csv.reader(file)
            # Skip the first line of the request.csv file because the first line contains column headings.
            next(reader)

            # Initialize totals outside the loop
            total_items = 0
            sub_total = 0

            for row in reader:
                # Extract the requested product number and quantity.
                product_number = row[0]
                quantity = int(row[1])

                # Use the requested product number to find the corresponding item in the products_dict.
                product = products_dict[product_number]  # This will raise KeyError if product_number is not found
                # Print the list of ordered items.
                product_name = product[1]
                product_price = float(product[2])
                print(f"{product_name}, Quantity: {quantity}, Price: {product_price}")

                # Accumulate the totals
                total_items += quantity
                sub_total += quantity * product_price

            # Print the summary after the loop
            print(f"Total items ordered: {total_items}")
            print(f"Subtotal: ${sub_total:.2f}")

            # Calculate the tax and print
            tax = 0.06 * sub_total
            print(f"Sales Tax: ${tax:.2f}")

            # Calculate the total cost of the order including tax and print
            total_cost = sub_total + tax
            print(f"Total: ${total_cost:.2f}")
            print()

            # Call the now() method to get the current date and time as a datetime object from
            # the computer's operating system.
            current_date_and_time = datetime.now()

            # Use an f-string to print the current day of the week and the current time.
            print("Thank you for shopping at Groceries R Us.")
            print(current_date_and_time.strftime("%a %b %d %H:%M:%S %Y"))

            # Write code to print at the bottom of the receipt the return by date that is seven days into the future.
            return_by_date = current_date_and_time.replace(day=current_date_and_time.day + 7)
            print(f"Return by: {return_by_date.strftime('%a %b %d %Y')}")

    except FileNotFoundError as file_not_found_err:
        print(file_not_found_err)
    except KeyError as key_err:
        print(f"Error: Product number {key_err} not found in the products dictionary.")
        
def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    # Create an empty dictionary to store the key-value pairs.
    dictionary = {}
    # Open the file for reading.
    with open(filename, "r") as file:
        # Create a CSV reader object.
        reader = csv.reader(file)
        # Skip the header row.
        next(reader)
        # Iterate over the rows in the CSV file.
        for row in reader:
            # Extract the key from the specified column index.
            key = row[key_column_index]
            # Store the entire row as the value in the dictionary.
            dictionary[key] = row
    # Return the dictionary.
    return dictionary

if __name__ == "__main__":
    main()