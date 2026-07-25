# Task 2
# The following program creates a username for a user. 
# It creates the username by taking the first letter of the 
# user’s first name and combining it with the user’s last name. 
# It will also allow the user to enter a password.

# The first name is entered without a space, for example, 
# Ah Seng is input as AhSeng.


# firstname = input("Please enter your first name: ")
# lastname = input("Please enter your last name: ")
# username = firstname[0] + lastname
# print("Your username is " + username)
# password = input("Please enter a password: ")

#==========================================================
# Open the file USERNAME.py
# 6       Edit the program so that the username is created 
#         using the first three letters of the first name, 
#         along with the last name.
# [1]
#_________________________________________________________

# firstname = input("Please enter your first name: ")
# lastname = input("Please enter your last name: ")
# username = firstname[:3] + lastname
# print("Your username is " + username)
# password = input("Please enter a password: ")




#==========================================================
# 7       The program needs to validate both the length of 
#         the password and whether the user has correctly 
#         re-entered their password.

# (a)    Edit the program to:
# ·       test whether the user has entered a password of eight characters or more.
# ·       output a suitable error message that asks the user to 
#         enter a password again if the password is less than 
#         eight characters, and repeat this until the user enters a valid password.
# [4]
#_________________________________________________________

# firstname = input("Please enter your first name: ")
# lastname = input("Please enter your last name: ")
# username = firstname[:3] + lastname
# print("Your username is " + username)

# while True:
#     password = input("Please enter a password: ")

#     if len(password) < 8:
#         print("Enter a password with 8 characters or more")
#     else:
#         break
    


    






#==========================================================
# (b)    Edit the program to:
# ·       asks the user to re-enter their password
# ·       check that the second entry of the password matches the first entry
# ·       output the message “Your password has been set.” If the password entries match
# ·       
#         otherwise, output the message 
#        “Password entries do not match. Please repeat the second entry of your password: “ 
#         and read in the password again, and repeat this until the password entries match.
# [5]
#_________________________________________________________

firstname = input("Please enter your first name: ")
lastname = input("Please enter your last name: ")
username = firstname[:3] + lastname
print("Your username is " + username)


while True:
    password = input("Please enter a password: ")

    if len(password) < 8:
        print("Enter a password with 8 characters or more")
    else:
        break

# happen after you set the first

while True:
    # password = input("Please enter a password: ")
    re_password = input("Please enter your password again: ")

    if re_password != password:
        print("Password entries do not match. Please repeat the second entry of your password:")
    else:
        print("Your password has been set.")
        break

    # if len(password) < 8:
    #     print("Enter your password with 8 characters or more")
    # elif re_password != password:
        