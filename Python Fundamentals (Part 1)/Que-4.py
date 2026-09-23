# Question 4:- The user enters a string containing a number, e.g. "45". Convert it to:
# - an integer
# - a float
# - a string again

# Print all three values with their types.

num = int(input("Enter: "))

integer_value = int(num)
float_value = float(num)
string_value = str(integer_value)

print(integer_value, type(integer_value))
print(float_value, type(float_value))
print(string_value, type(string_value))