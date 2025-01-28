"""
open(filename, mode="rt")
Open a file and return a corresponding file object.
filename is the name of the file to be opened.

mode is an optional string that specifies the mode in which the file will be opened. 
It defaults to "rt" which means open for reading in text mode. Other common values are "wt" for writing
 a text file (truncating the file if it already exists), and "at" for appending to the end of a text file that already exists 
 (and creating and writing to a text file that doesn’t exist).
"""

city_name = "Accra"
elevation = 61
population = 4200000

# Open a text file named cities.txt in append mode.
with open("cities.txt", "at") as cities_file:

    # Print a city's name and information to the file.
    print(city_name, file=cities_file)
    print(f"{elevation}, {population}", file=cities_file)