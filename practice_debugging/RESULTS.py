################################################################
# The following program collates the names and scores of students in a class.

# The program validates that the score is from 0 to 100 inclusive, 
# and also computes and outputs:

# number of scores entered
# number of students who score distinction (75 or more)
# number of students who failed (below 50)
# average score in the class
# The program allows a user to continue entering the names and scores 
# until the user enters the letter 'N' when prompted.

# There are several syntax errors and logical errors in the program.


name_list = []
mark_list = []
dist_list = []
pass_list = []
fail_list = []
count = 0 #6 count should start at 0

flag = True
while flag == True: #4 False should be True
    name = input("Enter student's name: ") #1 '' should be ""
    name_list += [name]
    while True:
        mark = int(input('Enter score of student: '))
        if mark >= 0 and mark <= 100: #10 or should be and
            break
        else:
            print('Invalid mark!')
    mark_list += [mark] #9 mark_list should be dedented
    count += 1
    if mark >= 75: #7 > should be >=
        dist_list += [name]
    elif mark >= 50:
        pass_list += [name]
    else:
        fail_list += [name] #8 () should be []
    more = input('Would you like to enter another score, Y or N?: ') #5 int should be removed
    if more == 'N':
        flag = False
average = round(sum(mark_list)/len(mark_list), 2) #2 max() should be sum() 
num_dist = len(dist_list)
num_fail = len(fail_list)
print("You entered " + str(count) + " scores.") #3 count should be converted to str
print(str(num_dist) + " students score distinction and " + str(num_fail) + " students failed.")
print("Average score is " + str(average)) # temp comment first... remember to uncomment later

print(pass_list)
print(fail_list)
print(dist_list)


# name_list = []
# mark_list = []
# dist_list = []
# pass_list = []
# fail_list = []
# count = 1

# flag = True
# while flag == False:
#     name = input('Enter student's name: ')
#     name_list += [name]
#     while True:
#         mark = int(input('Enter score of student: '))
#         if mark >= 0 or mark <= 100:
#             break
#         else:
#             print('Invalid mark!')
#         mark_list += [mark]
#     count += 1
#     if mark > 75:
#         dist_list += [name]
#     elif mark >= 50:
#         pass_list += [name]
#     else:
#         fail_list += (name)
#     more = int(input('Would you like to enter another score, Y or N?: '))
#     if more == 'N':
#         flag = False
# average = round(max(mark_list)/len(mark_list), 2)
# num_dist = len(dist_list)
# num_fail = len(fail_list)
# print("You entered " + count + " scores.")
# print(str(num_dist) + " students score distinction and " + str(num_fail) + " students failed.")
# print("Average score is " + str(average))