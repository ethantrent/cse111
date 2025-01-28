# ask the user to input a number (angle) between 0 and 359
# set the value as a float number
# "What's you GPS angle direction? (0-359) "
# verify if the input range is valid
# if not, ask the user to start the program again
# based on the angle use a set of if statements to
# determine the direction (N, NE, E, SE, S, SW, W, NW)
# print the direction the user is going to
# "According to the given angle, you are going to {direction}."

angle = float(input('What is your GPS angle direction (0-359)?: '))

if angle >= 0 and angle < 22.5:
    direction = 'North'
elif angle >= 45:
    direction = 'North East'
elif angle >= 90:
    direction = 'East'
elif angle >= 135:
    direction = 'South East'
elif angle >= 180:
    direction = 'South'
elif angle >= 225:
    direction = 'South West'
elif angle >= 270:
    direction = 'West'
elif angle >= 315:
    direction = 'North West'

print (f'According to the given angle, you are going to {direction}')
