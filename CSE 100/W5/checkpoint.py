# Write a program that asks the user for two integers.
# Then, write three separate if/else statements.
# Have the program ask the user for their favorite animal. 
# Verify that it works regardless of the capitalization.

first_number = int(input('What is the first number? '))
second_number = int(input('What is the second number? '))

if first_number > second_number:
    print ('The first number is greater')
else:
    print ('The first number is not greater')

if first_number == second_number:
    print ('The numbers are equal')
else:
    print ('The numbers are not equal')

if second_number >= first_number:
    print ('The second number is greater')
else:
    print ('The second number is not greater')

print ()

fav_animal = input('What is your favorite animal? ')
if fav_animal.lower() == 'panda':
    print ("That's my favorite animal too!" )
else:
    print ('That one is not my favorite')