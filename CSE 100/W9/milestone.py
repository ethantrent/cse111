# Have menu system that repeats until the user chooses quit.

# Create a list that will store the names of the items in the shopping cart.

# Complete the option to add the name of the item to the list.

# Complete the option to display the names of the items in the list.

# Store prices as well as names.

# Change the add functionality to also ask for and store the price of the item.

# Change the display functionality to also display the prices of the items.

# When displaying the items, display a number in front of each item. The numbers should start with 1.

# Complete the option to display the total amount of the prices of all the items in the shopping cart.

# Whenever prices are displayed, they should be shown to two decimal places and include the appropriate currency symbol (for example $, €, etc.)

# Complete the option to remove an item from the shopping cart.

# When removing an item, you should verify the following:

# Both the item name and price are removed from their respective lists.

# The number the user enters should be converted to a 0-based index and checked to make sure it is within the bounds of the list.

# The program allows you to remove any item from the list including the first one and the last one. 
# (Sometimes, if you have a bug in your project you might not allow removing the last item as you should.)

# Storing extra information, such as the quantity of the items in the list

print ('Welcome to the Shopping Cart Program!')

shopping_cart = []
prices = []
quantities = []
action = ''
total = 0

while action != '5':
    action = input('\nPlease Select One of The Following: \n1. Add an item to the cart \n2. View the cart \n3. Remove an item from the cart \n4. Compute total \n5. Quit \nPlease enter an action: ')
    if action == '1':
    # Add an item to the cart
        item = input('\nWhat item would you like to add? ')
        shopping_cart.append(item)
        price = input(f'What is the price of {item}? $')
        prices.append(float(price))
        quantity = input(f'How many {item} would you like to add? ')
        quantities.append(int(quantity))
        print (f" {quantity} '{item}' has been added to the cart ")
    # View the cart
    elif action == '2':
        print('\nShopping Cart:')
        for i in range(len(shopping_cart)):
            item = shopping_cart[i]
            price = prices[i]
            quantity = quantities[i]
            print(f'{i+1}. {quantity} {item} - ${price:.2f}')
    # Remove an item from the cart
    elif action == '3':
        index = int(input('\nEnter the index of the item you want to remove: ')) - 1
        if index < 0 or index >= len(shopping_cart):
            print('Invalid index. Please try again.')
        else:
            item = shopping_cart.pop(index)
            price = prices.pop(index)
            print(f"'{item}' has been removed from the cart.")
    # Compute total
    elif action == '4':
        for i in range(len(shopping_cart)):
            total += prices[i] * quantities[i]
        print(f'\nTotal price: ${total:.2f}')
    # Quit
    elif action == '5':
        print('Thank you for using the Shopping Cart Program!')
    else:
        print('Invalid input. Please try again.')

