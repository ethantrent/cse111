# No one under 36 inches may ever ride, either by themselves or with another rider.
# Normally, two riders sit in the car together. A single rider can only ride if they are 
# at least 18 years old and are at least 62 inches tall.
# If there are two riders and one of them is at least 18 years old, they may ride together.

# Stretch

# If there are two riders, but neither one is at least 18 years old,
# they may still ride as long as they are both at least 12 years old and at least 52 inches tall.
# If a person is age 12–17, ask if that person has a golden passport. 
# If they do, they should be treated as if they were 18 years old for the sake of all rules. 
# (Don't forget to apply this to the single rider case.)
# If there are two riders, but neither one is at least 18 years old, 
# they may still ride if one rider is at least 16 years old and the other is at least 14. 
# (Keep in mind that the first rider may be the younger of the two or they may be the older of the two.)

can_ride = False

age_1 = int(input('What is the age of the rider? '))
height_1 = int(input ('What is the height of the rider? '))
# Stretch 1
if age_1 >= 12 and age_1 > 18:
    golden_1 = input ('Does this rider have a golden passport (yes/no) ?').lower().strip()
second_rider = input('Is there a second rider (yes/no)? ').lower().strip()
if second_rider == 'yes':
    age_2 = int(input ('What is the age of the second rider? '))
    height_2 = int(input ('What is the height of the second rider? '))
    if age_1 >= 12 and age_1 > 18:
        golden_2 = input ('Does this rider have a golden passport (yes/no) ?').lower().strip()
    # Rule 1 Under 36in
    # No one under 36 inches may ever ride, either by themselves or with another rider.
    if height_1 <36 and height_2 <36:
        can_ride = False
    # Rule 3 
    # If there are two riders and one of them is at least 18 years old, they may ride together.
    else:
        if age_1>= 18 and age_2 <=18 and height_2 >= 36 or golden_1 == 'yes' or golden_2 == 'yes':
            can_ride = True
        else:
            can_ride = False
# Rule 2 Single rider
else:
    if age_1 >= 18 and height_1 >= 62:
        can_ride = True 
    else:
        can_ride = False
if can_ride:
    print ('Enjoy the ride!')
else:
    print ('Sorry, you may not ride.')
