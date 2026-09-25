# Question 10:- Let’s create a “Number Guessing Game”. Given a secret number (already decided by you), write a program that asks the user to guess it and prints:

# "Too high" if the guess is above the number
# "Too low" if the guess is below
# "Correct!" if the guess matches

guess_no = 7

guess = int (input("Guess the secret number: "))

if guess > guess_no:
    print("Too high")

elif guess < guess_no:
    print("Too low")

else:
    print("Correct!")
