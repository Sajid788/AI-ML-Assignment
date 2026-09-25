# Question 1:- Write a program that takes salary as input. Using conditional statements, calculate the final tax rate based on these rules:

# If salary < 30,000 → 5%
# If salary is 30,000–70,000 → 15%
# If salary > 70,000 → 25%

salary = float(input("Enter your salary value: "))

if salary < 30000:
    tax = 5
elif salary <= 70000:
    tax= 15
else:
    tax = 25

print(f"Your tax rate is {tax}%")