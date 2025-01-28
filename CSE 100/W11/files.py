# open and reading files
with open("candies.txt", 'r') as candies_file:
    for line in candies_file:
        print(line)

# .strip() removes "space" in the form of regular spaces, tab characters, or newline characters
old_line = "    This is a line with spaces and a newline character\n"
clean_line = old_line.strip()

print(clean_line)

# .split() that can split a string up based on whatever character you define that separates the pieces.
sentence = "I will go and do"

words = sentence.split(" ")
# The variable "words" is now a list that contains each word.

# You can iterate through each word and do something with it, such as display it:
for word in words:
    print(word)

