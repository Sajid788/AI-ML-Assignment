# Question 7:- Write a program that takes a string from the user and prints the number of spaces in the string.

word = input("Enter here the string: ")

count = 0

for char in word:
    if char == " ":
        count = count + 1
print(count)