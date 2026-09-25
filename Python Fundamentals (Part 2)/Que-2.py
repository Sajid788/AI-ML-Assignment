# Question 2:- Write a function that takes two integers a and b and prints all even numbers between them (inclusive).

def even_numbers(a, b):
    for num in range(a, b + 1):
        if num % 2 == 0:
            print(num)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

even_numbers(a, b)