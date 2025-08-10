message = "Hello World"
print(message)
print (len(message)) # returns length of string
print(message[0]) # use index to return character aka slicing
print(message[0:5]) #return range of characters (Hello)
    # inclusive  exclusive
print(message[6:])

print(message.lower()) # method used to lower characters
print(message.upper())
print(message.count("l")) # returns count of argument

greeting = 'Hello'
name = 'Ethan'

text = greeting + " " + name # concat
print(text)
print(f"{greeting}, {name}") # f-string