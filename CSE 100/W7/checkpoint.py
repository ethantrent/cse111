number = int(input('Please input a positive number: '))

while number < 0:
    print ('Sorry, that is a negative number. Please try again.')
    number = int(input('Please input a positive number: '))
print (f'The number is: {number}')


answer = input('May I have a piece of candy? ').lower().strip()

while answer == 'no':
    answer = input('May I have a piece of candy? ').lower().strip()
print ('Thank you.')    