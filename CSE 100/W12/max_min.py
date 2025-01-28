# finding the largest number in a list of numbers

numbers = [42, 25, 18, 83, 23, 85, 38, 2]

largest_so_far = numbers[0]

for number in numbers:
    if number > largest_so_far:
        # This number is larger than the largest we had seen so far

        # So it is now the largest we've seen
        largest_so_far = number

# Now, after the loop we can display it:
print(f"The largest is: {largest_so_far}")

# finding the smallest number in a list of numbers

numbers = [42, 25, 18, 83, 23, 85, 38, 2]

smallest_so_far = numbers[0]

for number in numbers:
    if number < smallest_so_far:
        # This number is smaller than the smallest we had seen so far

        # So it is now the smallest we've seen
        smallest_so_far = number

# Now, after the loop we can display it:

print(f"The smallest is: {smallest_so_far}")

# keeping track of the largest and smallest numbers in a list of numbers

shopping_cart = [
    ["Chips", 2.99],
    ["Bread", 2.50],
    ["Milk", 3.19],
    ["Ice Cream", 6.99],
    ["Cheese", 5.99],
    ["Candy bar", 0.99]
]

# find the maximum price in the shopping cart

max_price = -1

for item in shopping_cart:
    price = item[1] # The price is the second part of the item

    if price > max_price:
        # This is the new max
        max_price = price

print(f"The maximum price is: {max_price}")

# find the name of the item that is the most expensive

max_price = -1
max_product = "" # It doesn't matter what you set this to, it just needs to be declared

for item in shopping_cart:
    product_name = item[0] # Product name is the first part
    price = item[1] 

    if price > max_price:
        # This is the new max
        max_price = price

        # Also save this product name as the max product
        max_product = product_name

print(f"The maximum price is: {max_price}")
print(f"The product with the maximum price is: {max_product}")