# Use if and also else
# Strings are case sensitive
price = input('How much did you pay? ')

price =  float(price)
if price >= 1.0:
    tax = .07
    print (f'Tax rate is: {tax}')
else:
    tax = 0
    print (f'Tax rate is: {tax}')

country = input('Enter the name of your home country: ')
if country.lower() == 'canada':
    print ('So you must like hockey!')
else:
    print ('You are not from Canada')