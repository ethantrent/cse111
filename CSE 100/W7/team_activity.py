# Step 1
# Start by asking the user for the magic number. We are letting the user pick the magic number for now, 
# but in future steps we will change this to have the computer generate a random number for us. 

# Step 2
# Now add a loop that keeps looping as long as the guess does not match the magic number.
# At this point, the user should be able to keep playing until they get the correct answer.

# There is a random number library included with Python that contains a number of different functions to 
# generate random numbers, depending on if you want integers, floating point numbers, and from different statistical distributions.

import random

# The only function you will need from this library is called randint. 
# To use it, you give it two numbers and it returns back a random number in that range.

keep_playing = 'yes'

while keep_playing == 'yes':
    magic_number = random.randint(1, 10)
    guess_count = 0
    guess = -1

    while guess != magic_number:
        guess = int(input('Guess the magic number: '))
        if guess > magic_number:
            print ('Lower')
            guess_count += 1
        elif guess < magic_number:
            print ('Higher')
            guess_count += 1

    print (f'You guessed it! It took {guess_count} tries!')
    keep_playing = input ('Would you like to play again? ').lower().strip()

# import random

# magic_number = random.randint(1, 100)

# # I need to start the variable "guess" at something, but I don't want to start it as
# # valid number that the computer may have chosen, so I'll start with -1
# guess = -1

# # Keep going as long as the guess doesn't match the magic number
# while guess != magic_number:
#     guess = int(input("What is your guess? "))

#     if guess < magic_number:
#         print("Higher")
#     elif guess > magic_number:
#         print("Lower")
#     else:
#         print("You guessed it!")

