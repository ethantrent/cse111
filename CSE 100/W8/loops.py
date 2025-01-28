people = ['Christian, Susan']

for name in people:
    print (name)

print()
# Both of these do the exact same thing

index = 0
while index < len(people):
    print (people[index])
    index += 1

# An example of how to print the whole list

items = ["crayon", "scissors", "paper", "glitter glue", "markers", "pens"]

for item in items:
    print(f"The item is: {item}")

# Example of using a range rather than typing out all the numbers
for number in range(10):
    print(number)

# This loop will start with 100, and go up to, but not including 200
for i in range(100, 200):
    print(i)

# This loop will do the same thing, but this time, it will count by 10's
for i in range(100, 200, 10):
    print(i)

# We can also have a loop inside a loop
for i in range(5):
    print(i)
    for j in range(10, 13):
        print(f"--{j}")

# You can also iterate each letter of a string
first_name = "Brigham"
for letter in first_name:
    print(f"The letter is: {letter}")

# Access a specific letter 
first_name = "Brigham"

fourth_letter = first_name[3] # Notice, using 3 instead of 4
print(fourth_letter) # outputs a 'g' on the screen

# rather than looping through letters, you can loop through the index numbers
word = "book"
number_of_letters = 4

for index in range(number_of_letters):
# i = index
    print(f"Index: {index} Letter: {letter}")

# you can let the computer find the length by using the len function
dog_name = input("What is your dog's name? ")
letter_count = len(dog_name)

print(f"Your dog's name has {letter_count} letters")