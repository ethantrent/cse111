print ('Please enter the following information: ')

print ()

first = input ('First name: ')
last = input ('Last name: ')
email = input ('Email address: ')
phone = input ('Phone number: ')
job = input ('Job title: ')
ID = input ('ID number: ')

print ()

print ('The ID Card Is: ')
print ('-' * 40)
print (f'{last.upper()}, {first.capitalize()}')
print (job.title())
print (f'ID: {ID}')

print ()

print (email.lower())
print (phone)
print ('-' * 40)