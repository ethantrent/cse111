#Full Name = "  JOSHUA STONE  "
#E-Mail = "josh.Stone#gmail.com"
#Address = "101 E Viking St, Rexburg, ID 83460"
#City = "rexburg???"
#State = "Id"
#ZIP = "83460-"
#Phone = "208-496-1411_"

# Clean the variables

full_name = ' JOSHUA STONE '
email = 'josh.Stone#gmail.com'
address = '101 E Viking St, Rexburg, ID 83460'
city = 'rexburg???'
state = 'Id'
zip = '83460-'
phone = '208-496-1411_'

# OR

print (f'Full Name: {full_name.title().rstrip(' ').lstrip(' ')}')
print (f'Email: {email.lower().replace('#', '@')}')
print (f'Address: {address.split(',')[0].strip()}')
print (f'City: {city.capitalize().rstrip('?')}')
print (f'State: {state.upper()}')
print (f'Zip: {zip.rstrip('-')}')
print (f'Phone: {phone.rstrip('_')}')
