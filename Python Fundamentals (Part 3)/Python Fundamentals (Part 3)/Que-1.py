# Question 1:- Ask the user for a string and check whether it is a palindrome or not.
# A palindrome is a string which is same when we read it forward & backward. 
# Eg -“madam”, “racecar” etc.
# Hint: A palindrome string is equal to the reversed version of the string. We can use a loop to reverse the string manually.

palindrom = str(input("Enter word which is palindrom or not: "))

reverse = ""

for char in palindrom:
    reverse = char + reverse
if(reverse == palindrom):
    print("palindrom")
else:
    print("Not palindrom")