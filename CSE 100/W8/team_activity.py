# Create a string variable to hold the word "Commitment".
word = 'commitment'
# specify the letter
favorite_letter = input('What is your favorite letter? ').lower().strip()

for letter in word:
    if letter.lower() == favorite_letter.lower():
        print(letter.upper(), end="")
        # End is used to print on the same line for word
    else:
        print(letter.lower(), end="")

print ()

for letter in word:
    if letter.lower() == favorite_letter.lower():
        print("_", end="")
        # print _ is used to replace the letter
    else:
        print(letter.lower(), end="")



# Stretch Challenge
quote = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost"
number = input ('Please enter a number: ')

