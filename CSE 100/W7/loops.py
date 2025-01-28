tip = float(input('Tip Amount: '))

# In order to repeat and create a loop, use a WHILE statement

while tip < 0:
    print ('Sorry, that is an invalid tip.')
    tip = float(input('Tip Amount: '))

# This causes the question to be asked again since the amount of invalid

print (f'You tipped {tip:.2f}')