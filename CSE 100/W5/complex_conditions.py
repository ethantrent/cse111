# Nesting  if statements using "and"
gpa = float(input('What is your GPA?: '))
lowest_grade = float(input('What was your lowest grade?: '))
if gpa >= 0.85 and lowest_grade >= 0.70:
    print ('Well Done')

# To remember results of a condition check, use Boolean varaibles
if gpa >= 0.85 and lowest_grade >= 0.70:
    honor_roll = True
else:
    honor_roll = False
# Somewhere later in the code
if honor_roll:
    print ('Well Done')

#Ex. Student makes honor roll IF average is >= 0.85
# AND lowest grade is not below 75
gpa = float(input('What is your GPA?: '))
lowest_grade = float(input('What is your lowest grade?: '))

if gpa >= .85 and lowest_grade >= .75:
    print ('Well Done')
    honor_roll = True
else:
    honor_roll = False