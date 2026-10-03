# Question 2:- Given a list of integers compute the average of all numbers in the list.

Number = [20, 40,80 ,90, 5]
sum = 0
for num in Number:
    sum = sum + num
average = sum / len(Number)
print("average of the list: ", average)