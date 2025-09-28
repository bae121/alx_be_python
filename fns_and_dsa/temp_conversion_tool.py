# temp_conversion_tool.py

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(f):
    return (f - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(c):
    return (c * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temp_input = input("Enter the temperature to convert: ")
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if temp_input.isnumeric():
    temp = float(temp_input)
    if unit.upper() == "C":
        print(temp, "°C is", convert_to_fahrenheit(temp), "°F")
    elif unit.upper() == "F":
        print(temp, "°F is", convert_to_celsius(temp), "°C")
    else:
        print("Invalid unit. Please enter 'C' or 'F'.")
else:
    print("Invalid temperature. Please enter a numeric value.")
