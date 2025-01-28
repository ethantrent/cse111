x = input
y = input
if x > 5 and y > 10:
    print ()
# This happens if both conditions are true
if x > 5 or y > 10:
    print()
# This happens if either one of the conditions are true
word = 'print'
if x > 5 and y < 10 and word == 'taco':
    print ()
# This happens if all conditions are true
if (x > 5 or x < -5) and y > 10:
    # In this case, x can either be greater than 5 or less than negative 5, and y must
    # always be greater than 10
    if x > 5 or x < -5 and y > 10: 
        print()
    # Without parentheses, the x < -5 and y > 10 conditions go together and both must be
    # true, unless x > 5, in which case the whole statement is true
if x == 5 or x == 6:
    print()
# This is the correct way to check

