# Write a program to convert from Fahrenheit to Celsius. Display the result to one decimal place of precision.

degrees_f = float(input ('What is the temperature in Fahrenheit? '))
degrees_c = (degrees_f - 32) * 5/9
print (f'The temperature in Celsius is {degrees_c:.1f} ')

# :.1f rounded the number to the first decimal place