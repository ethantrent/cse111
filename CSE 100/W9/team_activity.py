# Compute the sum, or total, of the numbers in a list.
# Compute the average of the numbers in a list.
# Find the maximum, or largest, number in a list.
# Stop when they enter 0
# Have the user enter both positive and negative numbers, then find the smallest positive number (the positive number that is closest to zero).
# Sort the numbers in the list and display the new, sorted list.


numbers = []

# List of numbers
number = int(input("Enter a number: "))
while number != 0:
    numbers.append(number)
    number = int(input("Enter a number: "))

# Sum
sum = 0
for number in numbers:
    sum += number
print(f"The sum is: {sum}")

# Average
average = sum / len(numbers)
print(f"The average is: {average}")

# Largest
largest = 0
for number in numbers:
    if number > largest:
        largest = number
print(f"The largest number is: {largest}")

# Smallest positive number
smallest = 999999999999
for number in numbers:
    if number < smallest:
        smallest = number
print(f"The smallest positive number is: {smallest}")

# Sorted list
numbers.sort()
print(f"The sorted list is: {numbers}")
