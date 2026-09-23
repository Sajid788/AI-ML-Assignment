# Question 7:- Ask the user for a temperature in Celsius as string input. Convert it to float, then calculate and print the temperature in Fahrenheit.
    
# Formula:
# Fahrenheit = (Celsius × 9/5) + 32

celsius = input("Enter temperature in Celsius: ")
celsius = float(celsius)
fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit:", fahrenheit)