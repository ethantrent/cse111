# Use a for loop to iterate through this list one by one and display each item on its own line
colors = ["red", "blue", "green", "yellow"]
# To access a specific element in the list, use the index number
color = colors[0]
print (color)

# While loop
i = 0
items = ['crayons','markers','pencils']

while i < len(items):
    print (items[i])
    i += 1
# This is the same as the for loop below, but cleaner and easier to read
# For loop
for item in items:
    print (item)

print ()

# Range
# Use a for loop to display the numbers 1–8, one number on each line as follows
for number in range(1,9):
    print (number)

print ()

# Use a for loop to display the even numbers (hint: count by two) 2–20
for even in range(2,21,2):
    print (even)

# String length
word = 'book'
number_of_letters = len(word)

for letter in word:
    print (number_of_letters)

# Looping through a string

first_name = 'John'
for letter in first_name:
    print (letter)

# Printing without new lines

print("This is line one.", end="")
print("This is line two.")

# prints "This is line one.This is line two."

