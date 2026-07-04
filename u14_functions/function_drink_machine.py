# The following program has a dictionary that contains drink flavours and their prices. 
# The program allows the user to:

# calculate the total price of drinks ordered based on the flavour and amount of cups
# add or remove flavour-price pairs
# The task is to edit the program code so that it
# - allows user to input whether they want to calculate the price of an order
# - the total price of an order can be output based on a dictionary
# - allows user to input whether they want to add or remove a flavour 
#   and its price in the dictionary
# - keeps running until the user inputs the desire to exit the program.

def admin_mode():
    print()

def cashier_mode():
    print()
# main

# pricing
price_flavour = {
    "coffee": 5.50,
    "vanilla": 4.50,
    "caramel": 6.50,
    "hazelnut": 4.00
}

# cashier interface
# mode = input("Select mode (A/C/E): ")
    
# For each of the sub-tasks, add a comment using the hash symbol # 
# at the beginning of your code to indicate the sub-task 
# that the program code belongs to. For example:

# # Task 2.1
# For all sub-tasks, you can assume that all user input is valid.

# Task 2.1
# Edit the program by adding to “cashier interface” so that it:

# keeps looping asking the user to enter ‘A’, ‘C’ or ‘E’.
# if the user enters ‘A’ or ‘a’, the program will call the admin_mode()
# if the user enters ‘C’ or ‘c’, the program will call the cashier_mode()
# if the user enters ‘E’ or ‘e’, the program will end.
# [3]
#___________________________________________________________

# while True validation

# if mode.upper() == "A" or "C" or "E"
# if mode.upper() in ["A","C","E"]

# cmds = ["A","C","E"]

# while True:
    
#     mode = input("Select mode (A/C/E): ").upper()

#     if mode == "A":
#         admin_mode()
#     elif mode == "C":
#         cashier_mode()
#     elif mode == "E":
#         break
#     else:
#         print("Invalid, Select mode (A/C/E):")


#___________________________________________________________
# Task 2.2
# Copy and paste your program from sub-task 2.1.

# Edit the function cashier_mode(), so that it:
# - add a paramter for the flavour of a drink
# - add a paramter for the the number of cups for that flavour
# uses the dictionary price_flavour and outputs the total price for the order.
# [3]
#___________________________________________________________

# def admin_mode():
#     print()
    
# def cashier_mode(flavour, quantity):
#     total_price = price_flavour[flavour] * quantity
#     print(f"${total_price :.2f}")

#     # from the dictionary, retrieve price for flavour



# # main

# # pricing
# price_flavour = {
#     "coffee": 5.50,
#     "vanilla": 4.50,
#     "caramel": 6.50,
#     "hazelnut": 4.00
# }

# while True:
    
#     mode = input("Select mode (A/C/E): ").upper()

#     if mode == "A":
#         admin_mode()
#     elif mode == "C":
#         flavour = input("What flavour?: ") # ask user to input flavour
#         amt = int(input("How many cups?: ")) # ask user to input quantity
#         cashier_mode(flavour, amt) ## pass in value for flavour and quantity

#     elif mode == "E":
#         break
#     else:
#         print("Invalid, Select mode (A/C/E):")




#___________________________________________________________
# Task 2.3
# Copy and paste your program from sub-task 2.2.

# Edit the function admin_mode(), that has no parameters, so that it:

# allows the user to add or remove a flavour of a drink and 
# its price in the dictionary price_flavour

# outputs the dictionary after adding or removing a flavour
# [4]
 #___________________________________________________________

def admin_mode():
    while True:
        a_or_r = input("Do you want to add or remove a drink?[+/-]: ").lower()
        if a_or_r == "+":
            add_f = input("Enter the flavour of the drink: ")
            add_p = float(input("Enter the price of the drink: "))
            price_flavour[add_f] = add_p
            print(price_flavour)
            break
        elif a_or_r == "-":
            del_f = input("Which flavour do you want to delete?: ")
            if del_f in price_flavour:
                del price_flavour[del_f]
                print(price_flavour)
            else:
                print("Enter a valid flavour")
            break
        else:
            print("Invalid comman, must be [+/-]")

    
def cashier_mode(flavour, quantity):
    total_price = price_flavour[flavour] * quantity
    print(f"${total_price :.2f}")

    # from the dictionary, retrieve price for flavour



# main

# pricing
price_flavour = {
    "coffee": 5.50,
    "vanilla": 4.50,
    "caramel": 6.50,
    "hazelnut": 4.00
}

while True:
    
    mode = input("Select mode (A/C/E): ").upper()

    if mode == "A":
        admin_mode()
    elif mode == "C":
        flavour = input("What flavour?: ") # ask user to input flavour
        amt = int(input("How many cups?: ")) # ask user to input quantity
        cashier_mode(flavour, amt) ## pass in value for flavour and quantity

    elif mode == "E":
        break
    else:
        print("Invalid, Select mode (A/C/E):")
