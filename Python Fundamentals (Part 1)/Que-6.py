# Question 6:- Write a program to swap the values of two numbers entered by the user.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("original value: ", a, b)

# swap
a, b = b, a

print("swap value: ", a, b)