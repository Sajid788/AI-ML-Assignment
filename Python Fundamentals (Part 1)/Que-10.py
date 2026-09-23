# Question 10:- Take a decimal number as input, for example 45.78, and output:
# Integer part → 45
# Fractional part → .78
# If you're solving them one by one, Q1 → Q10 is the exact order from your assignment.

num = float(input("Enter decimal number: "))

interger_part = int(num)
fraction_part = num - interger_part

print('integer part',interger_part)
print('fraction part',fraction_part)
print('fraction part',round(fraction_part,2))

