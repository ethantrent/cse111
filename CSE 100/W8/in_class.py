# Write a program that uses a "for loop" to count the words, vowels, and consonants in a scripture: D&C 132:7.

scripture = 'And verily I say unto you, that the conditions of this law are these: All covenants, contracts, bonds, obligations, oaths, vows, performances, connections, associations, or expectations, that are not made and entered into and sealed by the Holy Spirit of promise, of him who is anointed, both as well for time and for all eternity, and that too most holy, by revelation and commandment through the medium of mine anointed, whom I have appointed on the earth to hold this power (and I have appointed unto my servant Joseph to hold this power in the last days, and there is never but one on the earth at a time on whom this power and the keys of this priesthood are conferred), are of no efficacy, virtue, or force in and after the resurrection from the dead; for all contracts that are not made unto this end have an end when men are dead.'

vowels = 0
consonants = 0
words = 0

for letter in scripture:
    if letter.lower() in 'aeiou':
        vowels += 1
    else:
        consonants += 1
    if letter == ' ':
        words += 1
print(f'The scripture has {words} words, {vowels} vowels, and {consonants} consonants.')



# Write a program that uses a "for loop" to reverse the string given by the 

reverse = ''
word = input ('Please enter a word: ')
for letter in word:
    reverse = letter + reverse
print(reverse)

# Write a program that uses nested "for loops" to print a multiplication table

