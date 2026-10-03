# Question 5:- Create a dictionary where:
# - Keys = student names
# - Values = marks (integer)
# Write a menu-based program where user presses a key ('A', 'B', 'C', 'D') depending on the operation they want to perform on the dictionary:
# 1. A - Add a student
# 2. B - Update marks
# 3. C - Search for a student
# 4. D - Display all students and marks

student = {}

while  True:
    print ("A - Add a student")
    print ("B - Update marks")
    print ("C - Search for a student")
    print ("D Display all student and marks")

    choice = input ("Enter your choice: ").upper()
    
    if choice == "A":
        name =  input ("Enter the student name: ")
        mark = int (input("Enter the student mark: ")) 
        student [name] = mark
        print("student added successfully")

    elif choice == "B":
        name = input ("Enter the student name : ")
        if name in student:
            mark = int (input("Enter the new mark: ")) 
            student[name] = mark
            print("Mark is updated successfully: ")
        else:
            print ("Student not found: ")

    elif choice == "C":
        name = input ("Enter the stude name: ")
        if name in student:
            print("Student", student[name])
        else:
            print("Student not found: ")

    elif choice == "D":
        for name, mark in student.items():
            print(f'name: {name}, marks: {mark}')

    elif choice == "E":
        print("Program Ended")
        break

    else:
        print("Invalid Input")
