# Write a program that determines the letter grade for a course according to the following scale:
# A >= 90
# B >= 80
# C >= 70
# D >= 60
# F < 60

grade = int(input('What is your grade percentage? '))
if grade >= 90:
    letter = 'A'
elif grade >= 80:
    letter = 'B'
elif grade >= 70:
    letter = 'C'
elif grade >= 60:
    letter = 'D'
else:
    letter = 'F'

sign = ''
last_digit = grade % 10
if last_digit >= 7:
    sign = '+'
elif last_digit < 3:
    sign = '-'
else:
    sign = ''

if grade >= 93:
    sign = ''
if letter == 'F':
    sign = ''

print (f'Your letter grade is {letter}{sign}')

if grade >= 70:
    print ('You passed the class!')
else:
    print ('You failed the class ;(')

























grade = int(input('What is your grade percent? '))
if grade >= 90:
    letter = 'A'
elif grade >= 80:
    letter = 'B'
elif grade >= 70:
    letter = 'C'
elif grade >= 60:
    letter = 'D'
else:
    letter = 'F'

print (f'Your letter grade is: {letter}')

if grade >=70:
    print ('Congratualtions! You passed the class!')
else:
    print ("Stay focused and you'll get there next time!")