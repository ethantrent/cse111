# Create two lists, one for the names of the bank accounts, and one for the balances.

# Ask the user for the name of the bank account and then for it's current balance. Keep looping until the user types "quit"

# for the name of an account. For each one, add the name and the balance to the appropriate list.

# Loop through the lists using an index and display the name of the account with the balance next to it.

# Compute and display the total balance in all of the accounts and the average balance.

print ('Enter the names of the bank accounts ans their balances (type: quit to finish):')

# Two lists
accounts = []
balances = []

account = ''
balance = ''

while account != 'quit':
# Ask user for account name
    account = input('What is the name of the account? ')
    if account != 'quit':
        accounts.append(account)
# Ask user for balance
        balance = float(input('What is the balance of the account? $'))
        balances.append(balance)
    if account == 'quit':
        break      
# Display account information
print ('\nAccount Information:')
for i in range(len(accounts)):
    account = accounts[i]
    balance = balances[i]
    print(f'{account}: ${balance}')

# Total balance and average balance
total_balance = sum(balances)
average_balance = total_balance / len(balances)

# Print total balance and average balance
print(f'\nTotal balance: ${total_balance:.2f}')

print(f'Average balance: ${average_balance:.2f}')