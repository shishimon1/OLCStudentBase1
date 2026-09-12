# A school requires a digital grade book to manage and analyze 
# student performance for a specific subject. 
# 
# You are required to develop a module that allows a teacher 
# to record student names and their respective marks in a centralized system.

# The program must ensure all entered marks fall within the 
# valid range of 0 to 100. Once the teacher has finished entering 
# all data, the program should automatically generate a class
# performance summary,providing the total student count, 
# the highest mark recorded, and the class average.

#=================================================
# Task 3.1
# Write a program that uses a while loop to collect student data. 
# The program must prompt for a Student Name and then a Mark (0 to 100). 
# The loop should terminate only when the word "quit" is
# entered for the StudentName. [2]
#=================================================

# while True:
#     stu_name = input("Enter the student's name: ")
#     if stu_name == "quit":
#         break
#     mark = int(input("Enter the mark of the student (0 to 100): "))



#=================================================
# Task 3.2
# Copy and paste your program from sub-task 3.1.
# For validation checks:
# - ensure the name contains alphabets only.
# - ensure the mark contains only numbers.
# - ensure the mark is between 0 and 100 inclusive.
# If the mark is invalid,display an error message and prompt 
# the user to re-enter the mark for that specific student. [4]
#=================================================
# while True:
#     while True:
#         stu_name = input("Enter the student's name: ")

#         if not stu_name.isalpha():
#             print("Name cannot have numbers")
#         else:
#             break

#     if stu_name == "quit":
#             break
    
#     while True:
#         mark = input("Enter the mark of the student (0 to 100): ")

#         if not mark.isdigit():
#             print("Mark must be a digit.")
#         elif int(mark) < 0 or int(mark) > 100:
#             print("Mark must be between 0 to 100.")
#         else:
#             break






#=================================================
# Task 3.3
# Copy and paste your program from sub-task 3.2.
# Store the validated name and mark in a dictionary named grade_book. 
# Once the loop ends, use the dictionary to display:
# - The total number of students recorded.
# - The highest mark achieved in the class.
# - The average mark, formatted to two decimal places. [4]
#=================================================
grade_book = {}

while True:
    while True:
        stu_name = input("Enter the student's name: ")

        if not stu_name.isalpha():
            print("Name cannot have numbers")
        else:
            break

    if stu_name == "quit":
            break
    
    while True:
        mark = input("Enter the mark of the student (0 to 100): ")

        if not mark.isdigit():
            print("Mark must be a digit.")
        elif int(mark) < 0 or int(mark) > 100:
            print("Mark must be between 0 to 100.")
        else:
            break

    grade_book[stu_name] = int(mark)
    print(grade_book)

highest = 0
total = 0

# alternative way if no .items()
# for key in grade_book: # retrieves the key
#     if grade_book[key] > highest:
#         highest = grade_book[key]

for key, value in grade_book.items():
    if value > highest:
        highest = value

    total = total + value

print(f"There are {len(grade_book)} amount of students recorded.")
print(f"Highest score is {highest}.")
print(f"Average score is {total / len(grade_book)}.")