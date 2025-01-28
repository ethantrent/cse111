def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")


greet("Ethan", "Trent")
greet("Alice", "Smith")


def main():
    # Ask the user for a temperature in Celsius.
    celsius = int(input("Enter a temperature in Celsius: "))

    # Convert the temperature to Fahrenheit.
    fahrenheit = function_to_fahrenheit(celsius)

    # Print the temperature in Fahrenheit.
    print(f"The temperature in Fahrenheit is {fahrenheit}.")


def function_to_fahrenheit(celsius):
    fahrenheit = (celsius * (9 / 5)) + 32
    return fahrenheit

main()


def main():
    # Ask the user for a temperature in Fahrenheit.
    fahrenheit = float(input("Enter a temperature in Fahrenheit: "))

    # Convert the temperature to Celsius.
    celsius = fahrenheit_to_celsius(fahrenheit)

    # Print the temperature in Celsius.
    print(f"The temperature in Celsius is {celsius}.")

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * (5 / 9)
    return celsius

main()


def miles_to_km(miles):
    km = miles * 1.60934
    return km