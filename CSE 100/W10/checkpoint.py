# Loop through the items in the regular way (for example, for thing in the_list) 
# and display each one to make sure you have the initial list built correctly.
# Add another loop to go through and print the items in the list, but this time, instead of using the for ... in syntax, 
# use an index (for example, for ... in range) and then access the item using the index and the square brackets. Print the index in front of the items like so: 0. Milk
# Ask the user for an index and a new shopping list item. Replace the item at that index with the new item. 
# Then, display the whole list again.

shopping_list = []
item = ''

print('Please enter the items of the shopping list (type: quit to finish): ')
# Loop through items in a regular way
while item != 'quit':
    item = input('Enter an item: ')
    if item != 'quit':
        shopping_list.append(item)
    else:
        break

# Print shopping list
print('\nThe shopping list is:')
for item in shopping_list:
    print(item)

# Another loop but print the index in front of the items
print ('\nThe shopping list with indexes is:')

for i in range(len(shopping_list)):
    item = shopping_list[i]
    print(f'{i}. {item}')

# Ask for index to replace
index = int(input('\nEnter the index of the item you want to replace: '))
new_item = input('Enter the new item: ')

# Replace the item at the index with the new item
shopping_list[index] = new_item

# Display the whole list again
print('\nThe shopping list with indexes is:')
for i in range(len(shopping_list)):
    item = shopping_list[i]
    print(f'{i}. {item}')





