# Question 7:- Design a program to continuously input a number n from the user and 
# print whether it is positive or negative until the user enters: “Quit”

while True:
    check_input = input("Enter a number or Quit to stop: ")
    if(check_input == "Quit"):
        break

    n = int(check_input)

    if n > 0:
        print("Positive")

    elif n < 0:
        print("Negative")

    else:
        print("Zero")