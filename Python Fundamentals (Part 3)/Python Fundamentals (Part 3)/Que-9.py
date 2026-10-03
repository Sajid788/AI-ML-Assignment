# Question 9:- Given a list, print all elements that appear more than once in the list.
# [Hint - use sets]

number = [2,5,6,7,9,3,8,9,3,6,2]

data = set()
dublicate = set()

for num in number:
    if num in data:
        dublicate.add(num)
    else:
        data.add(num)
print(dublicate)