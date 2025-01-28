the_list = []

first = the_list[0] # gets the first item
second = the_list[1] # gets the second item

index = int(input("Which index would you like to get? "))
user_choice = the_list[index] # gets the item at the index the user typed

# You can find out how many elements are in a list
books = ['Python Crash Course', 'Automate the Boring Stuff with Python', 'Python for Data Analysis']
number_of_books = len(books)


for i in range(len(books)):
    book = books[i]
    print(book) # print each book to the screen.

for i in range(len(books)):
    book = books[i]
    print(f"{i}. {book}") # print each book to the screen with the index.

# There are a few different ways to remove items from a list
the_list.pop(3) # Removes the item at index 3

the_list.pop() # Removes the last item

# two lists to loop through the indexes that correspond
names = []
numbers = []

# ...
# Code here that populates the two lists
# ...

for i in range(len(names)):
    name = names[i]
    number = numbers[i]

    print(f"{name} - {number}")