# Write a function to calculate and return the wind chill based on a given temperature and wind speed.
# Write a function to convert from Celsius to Fahrenheit. The formula for this conversion is to multiply the Celsius temperature by (9/5) and then add 32.
# Allow the user to enter the temperature in Celsius of Fahrenheit. If they provide it in Celsius, first convert it to Fahrenheit before using the formula above.
# Loop through wind speeds from 5 to 60 miles per hour, incrementing by 5, and calculate and display the wind chill for each of these wind speeds.
# Display the wind chill value to 2 decimals of precision.

# Write a function to calculate and return the wind chill based on a given temperature and wind speed.
def wind_chill(temp, wind_speed):
    return 35.74 + 0.6215*temp - 35.75*(wind_speed**0.16) + 0.4275*temp*(wind_speed**0.16)

# Write a function to convert from Celsius to Fahrenheit. The formula for this conversion is to multiply the Celsius temperature by (9/5) and then add 32.
def celsius_to_fahrenheit(temp):
    return temp * (9/5)

# Allow the user to enter the temperature in Celsius of Fahrenheit. If they provide it in Celsius, first convert it to Fahrenheit before using the formula above.
temp = float(input("Enter the temperature: "))
unit = input("Enter the unit (C or F): ").upper()
if unit == "C":
    temp = celsius_to_fahrenheit(temp)

# Loop through wind speeds from 5 to 60 miles per hour, incrementing by 5, and calculate and display the wind chill for each of these wind speeds.
for wind_speed in range(5, 61, 5):
    print(f'At a wind speed of {wind_speed} mph, the wind chill is {wind_chill(temp, wind_speed):.2f}')

# Display the wind chill value to 2 decimals of precision.
# Done above