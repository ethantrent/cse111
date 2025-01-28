# Ask the user for the current checking balance
# Keep asking the user about their current account debits (expenses)
# Make sure they have balance for this payment
# If the checking balance will be lower than the balance, deny it
# Update the balance
# Print the balance
# Ask if they want to make another payment
# If yes, repeat the process
# If not, thanks the user
# Show the current balance and leave

repeat = 'yes'

while repeat == 'yes':

    balance = float(input ('Current Checking Balance: '))
    answer = float(input ('Would you like to make a payment? (yes = 1, no = 2) '))
    
    while answer == 1:
        spend = float(input ('How much would you like to spend? '))
        if spend > balance:
            print ('Denyied, try again.')
        elif spend <= balance:
            balance -= spend
        print (f'Your balance is now {balance:.2f}')
        repeat = input ('Would you like to make another expense (yes or no)? ').lower().strip()
        if repeat == 'no':
            print (f'Your balance is now {balance:.2f}')
            break  
    print (f'Your balance is now {balance:.2f}')
    break