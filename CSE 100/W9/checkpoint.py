# Ask the user for the names of their friends
# display each of the friends in the list
# stop asking for friends when the user types "end"
# display print "Your friends are: " followed by the list of friends

friends = []
friend = input('Enter the name of a friend: ').lower().strip()

while friend != 'end':
    friends.append(friend)
    friend = input('Enter the name of a friend: ').lower().strip()

print('\nYour friends are: ')

for friend in friends:
    print(friend.title())

