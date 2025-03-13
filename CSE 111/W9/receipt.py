import csv

def main():
    # Call the read_dictionary function and store the compound dictionary in a variable named products_dict.
    products_dict = read_dictionary("products.csv", 0)
    # Print the products_dict.
    print("All Products:")
    print(products_dict)
    print()
    # Open the request.csv file for reading.
    with open("request.csv", "r") as file:
        # Create a CSV reader object.
        reader = csv.reader(file)
        # Skip the first line of the request.csv file because the first line contains column headings.
        next(reader)
        # Use a loop that reads and processes each row from the request.csv file.
        for row in reader:
            # Extract the requested product number and quantity.
            product_number = row[0]
            quantity = row[1]
            # Use the requested product number to find the corresponding item in the products_dict.
            product = products_dict.get(product_number)
            if product:
                # Print the product name, requested quantity, and product price.
                product_name = product[1]
                product_price = product[2]
                print(f"Product: {product_name}, Quantity: {quantity}, Price: {product_price}")

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