# only one condition will occur
providence = input ('What is your providence? ')
# you can specify the country with:
# if country == 'Canada'
    #if providence == 'Alberta':
if providence == 'Alberta':
    tax = 0.05
elif providence == 'Nunavut':
    tax = 0.05
# Since the first two both have the same tax rate, it could be displayed as:
#if providence == 'Alberta' or providence == 'Nunavut':
    #tax = 0.05
elif providence == 'Ontario':
    tax = 0.13
else:
    tax = 0.15
# if we had more than two with the same tax, then it could be displayed as:
# if providence in('Alberta', 'Nunavut', 'Ontario'):