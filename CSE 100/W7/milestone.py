# Have a secret word stored in the program.
# Prompt the user for a guess
# Continue looping as long as that guess is not correct.
# Calculate the number of guesses and display it at the end.
# You do not need to have any hints at this point.

# Add the hints according to the rules above.
# Add a check to verify that the length of the guess is the same as the length of the secret word. 
# If it is not, display a message. If they are the same, then proceed to give the hint.
# Use a loop to generate the initial hint.
# Make sure to account for the following in your hints:
# Letters that are not present at all in the secret word (underscore _).
# Letters that are present in the secret word, but in a different spot (lowercase).
# Letters that are present in the secret word at that exact spot spot (uppercase).

import random

# Have a secret word stored in the program.
list = ["light", "shade", "color", "paint", "blend"]
secret = random.choice(list)
guesses = 10
guess_count = 0

print ('Welcome to the word guessing game!')
print ('The word is 5 letters.')

print ()

while guesses > 0:
# Prompt the user for a guess
    guess = input(f'You have {guesses} guesses left. What is your guess? ').lower().strip()

    if len(guess) != 5:
        print('\nYour guess was not the correct amount of letters, try again.')
        continue
        # Continue looping as long as that guess is not correct.
    elif guess != secret:
        print ('\nYour guess was not correct, try again.')
        guesses -= 1
# Calculate the number of guesses and display it at the end.
        guess_count += 1
    else:
        print ('\nCongratulations! You guessed it!')
        print (f'It took {guess_count} guesses!')
        break  
    # Feedback storage
    feedback = ["_"] * 5

    # Check for correct letters in the correct position
    for i in range(5):
        if guess[i] == secret[i]:
            feedback[i] = guess[i].upper()  # Correct letter in the correct position

    # Check for correct letters in the wrong position
    for i in range(5):
        if guess[i] != secret[i] and guess[i] in secret:
            feedback[i] = guess[i].lower()

    # Show feedback
    print("Feedback: " + " ".join(feedback))

if guesses == 0:
    print (f' Sorry, you ran out of attempts. The word was {secret}!')
