# Task 5 

# Open a new Jupyter notebook and save the file as: 
# TASK5_<your name>_<centre number>_<index number>.ipynb 

# The task is to write a program that checks whether a word that is input is a palindrome. 
# A word is a palindrome if it is the same when it is read forwards and backwards. 

# For example: 
# the word 'level' is a palindrome because it is the 
#    same when read forwards and backwards 
# the word 'orange' is not a palindrome because it is 'orange' 
#    when read forwards and 'egnaro' when read backwards. 
# For each of the sub-tasks, add a comment using the hash symbol '#' 
#     at the beginning of your code to indicate the sub-task that the 
#     program code belongs to. For example: 


# Output: 
# All code should have appropriate comments and all identifiers should be appropriately named. 
# [4] 

# ---------------------------------------------------
# Task 5.1 
# Write the function midpoint() to find the midpoint of the word. The function must: 
# take a word as a parameter calculate the midpoint of the word. 
# This is the position of the character that is in the centre of the word. 
# If the word does not have a central character, the character to the 
# left of the centre is selected. 

# return the position of the character in the midpoint of the 
# word or return 0 if the word string is empty. 

# For example: 
# in the word 'melon' the character 'l' is the midpoint, so 2 is returned 
# in the word 'pineapples' the character 'a' is the midpoint, so 4 is returned. 
# [5] 

# Save your program. 
# ---------------------------------------------------

# len of word // 2 and round down
# import math

def midpoint(word):
    index = len(word) // 2 # floor divide to get the index

    if len(word) == 0:
        return 0
    elif len(word) % 2 == 0:
        return index - 1 # for even need to shift left 1
    else:
        return index



# print(midpoint("hannah")) # 2 even
# print(midpoint("melon"))  # 2
# print(midpoint("level"))
# print(midpoint("pineapples")) # 4 # even
# print(midpoint("")) # 0






# ---------------------------------------------------
# Task 5.2 
# Copy and paste your program from sub-task 5.1. 
# Extend your program by writing the function palindrome() to find out 
# whether a word is a palindrome. The function must: 
#       take a word as a parameter 
#       calculate whether the word is a palindrome or not a palindrome 

# return: 
#   "Palindrome" if the word is a palindrome 
#   "Not palindrome" if the word is not a palindrome 
#   "No word entered" if the word is an empty string. 

# Your function must use the function midpoint() to help find out if a 
# word is a palindrome. You must not reverse any strings to 
# check whether the word is a palindrome. 
# [10] 

# Save your program. 
# ---------------------------------------------------
def palindrome(word):
    middle = midpoint(word)
    if middle == 0:
        return "No word entered"

    elif len(word) % 2 == 0: # if even length
        for i in range(middle + 1):
            # print(f"{word[middle - i]} : {word[middle + i + 1]}")
            if word[middle - i] != word[middle + i + 1]: # need to account +1 for right side
                return "Not palindrome"
            
        return "Palindrome"

    else:
        for i in range(middle + 1):
            if word[middle - i] != word[middle + i]: # compare the indexed characters
                return "Not palindrome"
                        
        return "Palindrome"
        
    # reversed = word[::-1]
    # if word == "":
    #     return "No word entered"
    # elif reversed == word:
    #     return "Palindrome"
    # elif reversed != word:
    #     return "Not palindrome"




print(palindrome("hannxh"))
print(palindrome("otto"))
print(palindrome("level"))
print(palindrome("melon"))
print(palindrome(""))





# ---------------------------------------------------
# Task 5.3 

# Copy and paste your program from sub-task 5.2. 
# Extend your program to create an interface that: 
#       takes a word as input and converts it to lower case 
#  uses the correct functions to output: 
#       whether the word is an empty string 
#       the character at the midpoint of the word 
#       whether the word is a palindrome or not a palindrome. 

# If the word is not a palindrome, the program must make the word into a 
# palindrome and output the palindrome. 

# For example, if the word hello is input, the program would output helloolleh 

# [6] 

# Save your JupyterLab notebook for Task 5. 
# ---------------------------------------------------

# 5.3


def palindrome(word):
    middle = midpoint(word)
    if middle == 0:
        return "No word entered"
    elif len(word) % 2 == 0:
        for i in range(middle + 1):
            # print(f"{word[middle - i]} : {word[middle + i + 1]}")
            if word[middle - i] != word[middle + i + 1]:
                return "Not palindrome"
            
        return "Palindrome"

    else:
        for i in range(middle + 1):
            if word[middle - i] != word[middle + i]:
                return "Not palindrome"
                        
        return "Palindrome"

word = input("Enter a word: ").lower()
check_p = palindrome(word)
check_m = midpoint(word)

if check_m == 0: # if return 0, means empty
    print(check_p)
else:
    print(f"The middle character is {word[check_m]}")
    print(f"{word} is {check_p}")




















