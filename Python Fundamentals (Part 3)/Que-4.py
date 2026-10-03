# Q4. Given a tuple of integers, create:
# - A tuple of all even numbers
# - A tuple of all odd numbers

tuple_No = (1,2,7,8,9,4)

even_no = ()
odd_no = ()

for num in tuple_No:
    if num % 2 == 0:
        even_no = even_no + (num,)
    else:
        odd_no = odd_no + (num,)

print("Even No", even_no)
print("Odd No", odd_no)