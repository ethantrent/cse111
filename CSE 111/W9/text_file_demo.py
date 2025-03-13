import csv

def main():
    dentist_dict = make_dict_from_csv_file("dentists.csv", 2) # 2 specifies the index of the phone number column
    print(dentist_dict)


def make_dict_from_csv_file(filename, key_index): # use file name as parameter into open and the key index
    dictionary = {}
    with open(filename, "rt") as file:
        # create a csv reader object
        csv_reader = csv.reader(file)
        # skip the first row of the csv file
        next(csv_reader)
        # iterate through each row in the csv file
        for line in csv_reader:
            key = line.pop(key_index) # remove the first element from the list and store it in key
            dictionary[key] = line # add the key and the rest of the list to the dictionary
    return dictionary

if __name__ == "__main__":
    main()