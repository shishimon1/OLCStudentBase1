# Open the file GROUPS.ipynb
# Copy the program into a new JupyterLab notebook and save the file as:

# TASK4_<your name>_<centre number>_<index number>.ipynb
# The program should put children into groups using the following rules:

# group 1 – if the first letter of the first name is between 
# A and M (inclusive) and they are older than 10 years

# group 2 – if the first letter of the first name is between 
# N and Z (inclusive) and they are older than 10 years

# group 3 – if they are 10 years or younger.
# The program allows a child’s first name and age to be entered. 
# It then stores the child’s first name in the correct group list. 
# The program loops until the user does not want to enter any more 
# children’s names or their ages. It then outputs the total number 
# of children, as well as the names of the children in each group.

# There are several syntax errors and logic errors in the program.


group_1 = []
group_2 = []
group_3 = []
count = 0 #4 add count
flag = True
while flag:
    first_name = input("Please enter the child's name: ").upper()
    first_letter = first_name[0] #1 first_name should be first_letter #5 index 0 should be index 1
    age = int(input("Please enter the child's age: ")) #2 logic error, convert age to int
    if first_letter >= "A" and first_letter <= "M" and age > 10: 
        group_1 = group_1 + [first_name]
    elif first_letter > "M" and age > 10: #6 logic error, or should be and #7 logic error, >= should be >
        group_2 = group_2 + [first_name]
    elif age <= 10: #8 logic error, < should be <=
        group_3 = group_3 + [first_name]
    count += 1 #4 add count out of if
    more = input("Do you have another child to enter, Y or N?: ")
    if more == "N": #3 logic error, Y should be N to end loop
        flag = False

print("You have entered the names of", count, "children") #4 flag should be count
print("The members of group 1 are", group_1)
print("The members of group 2 are", group_2)
print("The members of group 3 are", group_3)


# This is the copy of the original code

# group_1 = []
# group_2 = []
# group_3 = []
# flag = True
# while flag:
#     first_name = input("Please enter the child's name: ").upper()
#     first_name = first_name[1]
#     age = input("Please enter the child's age: ")
#     if first_letter >= "A" and first_letter <= "M" and age > 10:
#         group_1 = group_1 + [first_name]
#     elif first_letter >= "M" or age > 10:
#         group_2 = group_2 + [first_name]
#     elif age < 10:
#         group_3 = group_3 + [first_name]
#         count += 1
#     more = input("Do you have another child to enter, Y or N?: ")
#     if more == "Y":
#         flag = False

# print("You have entered the names of", flag, "children")
# print("The members of group 1 are", group_1)
# print("The members of group 2 are", group_2)
# print("The members of group 3 are", group_3)