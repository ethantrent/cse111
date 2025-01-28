# The rental car company offers three car types: Economy, Midsize, and Luxury.
# The base rental cost per day for each car type is: Economy ($30), Midsize ($40), Luxury ($60).
# If the rental duration is longer than 7 days, a 10% discount is applied to the base rental cost.
# If the driver is under 25 years old, an additional young driver fee of $10 per day is charged.
# Additional services include GPS navigation ($5 per day) and child seats ($3 per day).
# If the total rental cost exceeds $500, an additional 8% tax is applied.
 
# 1. Ask teh user for: car type, duration, age, services
# 2. Determine the base rental cost per day based on the car type.
# 3. Calculate the base rental cost for the given rental duration.
# 4. Apply a 10% discount if the rental duration is longer than 7 days.
# 5. Add a young driver fee if the driver is under 25 years old.
# 6. Add the cost of additional services (GPS and child seats) based on the rental duration.
# 7. Apply an 8% tax if the total rental cost exceeds $500.
# 8. Return the total rental cost.

# #Step 2
# economy = 30
# midsize = 40
# luxury = 60

# # Step 1
# car_type = (input('What car type would you like (Economy/Midsize/Luxury)? ')).lower().strip()
# duration = int(input('How many days will you be renting the car? '))
# age = int(input('How old is the driver? '))
# #Step 6
# gps_needed = (input('Would you like to include a GPS (yes/no)? ')).lower().strip()
# child_seat_needed = (input('Would you like to add a child seat (yes/no) ?')).lower().strip()

# # Step 3
# rental_cost = 0
# if car_type == 'economy':
#     rental_cost = car_type * duration
# if car_type == 'midsize':
#     rental_cost = car_type * duration
# if car_type == 'luxury':
#     rental_cost = car_type * duration

# # Step 4
# # 10% discount for over 7 days
# if duration > 7:
#     rental_cost *= .90

# # Step 5
# # Add a young driver fee of $10 if under 25
# if age < 25:
#     young_driver_fee = 10 * duration
#     rental_cost += young_driver_fee

# # Step 6
# # GPS for $5 per day and $3 per day for child seats
# gps_cost = 5 * duration * gps_needed

# child_seat_cost = 3 * duration * child_seat_needed

# rental_cost += gps_cost + child_seat_cost

# # Step 7
# # 8% tax if rental cost exceeds $500
# if rental_cost > 500:
#     rental_cost *= 1.08

# # Step 8
# # Print out total
# print (f'The total rental cost is {rental_cost:.2f}')


# costs
economy_cost = 30
midsize_cost = 40
luxury_cost = 60
rental_cost = 0
 
# car type
car_type = int(input("Enter the car type (1=Economy, 2=Midsize, or 3=Luxury): "))
 
if car_type not in (1,2,3):
    print("Invalid car type")
    exit()
 
# rental days
rental_days = int(input("Enter the rental duration (in days): "))
 
if rental_days <= 0:
    print("Invalid rental duration")
    exit()
 
# driver age
driver_age = int(input("Enter the driver's age: "))
 
if driver_age < 0:
    print("Invalid driver's age")
    exit()
 
# gps needed
gps_needed = int(input("GPS needed? (0 for no, 1 for yes): "))
 
if gps_needed not in (0, 1):
    print("Invalid input for GPS")
    exit()
 
# child seets
child_seats_needed = int(input("Child seats needed? (0 for no, 1 for yes): "))
 
if child_seats_needed not in (0, 1):
    print("Invalid input for child seats")
    exit()
 
# rental cost (1=Economy, 2=Midsize, or 3=Luxury)
if car_type == 1:
    rental_cost = economy_cost * rental_days
if car_type == 2:
    rental_cost = midsize_cost * rental_days
if car_type == 3:
    rental_cost = luxury_cost * rental_days
 
# Apply 10% discount
if rental_days > 7:
    rental_cost *= 0.9  
 
# Apply additional young driver fee of $10 per day
if driver_age < 25:
    young_driver_fee = 10 * rental_days
    rental_cost += young_driver_fee
 
# GPS ($5 per day)
gps_cost = 5 * rental_days * gps_needed
 
# child seats ($3 per day).
child_seats_cost = 3 * rental_days * child_seats_needed
 
rental_cost += gps_cost + child_seats_cost
 
# Apply 8% tax if costs over $500
if rental_cost > 500:
    rental_cost *= 1.08  
 
print(f"The total rental cost is: ${rental_cost:.2f}")

