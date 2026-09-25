# Question 3:- Write a function that prints the digits of a number n.
# For example: n = 312
# There are 3 digits: 3, 1, and 2, and we need to print them.
# Hint:The rightmost digit of a number N is N % 10.
# To remove the rightmost digit, we can do N = N / 10.

def print_digit(n):
    result = 0
    while n > 0:
        digit = n % 10
        result = result * 10 + digit
        # print(digit)
        n = n//10
    print(result)
n = int(input("Enter the value: "))

print_digit(n)