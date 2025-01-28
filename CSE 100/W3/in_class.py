# number of friends
friends = int(input('How many friends are going to the activity? '))
# number of seats
seats = int(input('How many seats on each vehicle? '))
# calculate number of vehicles needed
vehicles_needed = (friends + seats) // seats
print (f'{vehicles_needed} vehicles needed')
# calculate number of loaded vehicles
loaded = friends // seats
print (f'{loaded} loaded vehicles')
# calculate number of remaining friends
remaining = friends % seats
print (f'{remaining} friends remaining')