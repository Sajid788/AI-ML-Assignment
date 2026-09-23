# Question 5:- Evaluate and print the result:
# x = 10 + 3 * 2 ** 2
# Then explain why the output is what it is based on the order of operations.

x = 10 + 3 *2 ** 2

print("x value: ", x)

# x value is = 22
# Python follows the order of operations:
# ** -> * / -> + -
# 10 + 3 * 2 ** 2
# 10 + 3 * 4
# 10 + 12
# 22
# so final ans is 22