# Strings can be stored as variables

first_name = 'Ethan '
print(first_name)

# You can also combine two strings with the + sign

last_name = 'Trent '
print(first_name + last_name)
print ('Hello '+ first_name + last_name)

# Functions may be used to modify stirngs

sentence = 'the dog is named sammy'
print (sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
print(sentence.count('a'))

# Put it all together and it looks something like this

first_name = input ('What is your first name? ')
last_name = input ('What is your last name? ')
print ('Hello ' + first_name.capitalize() + ' ' + last_name.capitalize())