# FUNCTIONS : UDF

## DEFINE A FUNCTION to say Hello
def hello():
    print("Hello")

# call the function (executes the function)
# hello()

def greeting(yourname): ### parameter - variable used inside function
    print(f"Hello, {yourname}")

# call the greeting function
# greeting("Kenneth")

### return.....
# calculate the area of a circle

# pi x r square

def area_circle(radius): # radius is a parameter
    area = 3.1415 * (radius ** 2)

    return(area)

# calculate the total area of all these circles...
# list_of_radius = [3.9,63.6,68.4,96.5,44.8]
# total_area = 0

# for circle in list_of_radius:
#     current = area_circle(circle)

#     total_area = total_area + current

# print(total_area)


###########################################################
# Part 2. IN-CLASS Practice Exercises

# Exercise 7: Greeting Multiple Users
# Write a function that takes a list of names and greets each one.


# Call the function with a list of names.
# greet_users(["Alice", "Bob", "Charlie"])

users = ["Alice","Bob","Charlie"]

def greet_user(user_list):
    for name in user_list:
        print(f"Hello {name}")


# calls the function
# greet_user(users)


#------------------------------------------------------------
# Exercise 8: Simple Calculator
# Write a function that takes two numbers and an operator (+, -, *, /)
# and returns the result of the calculation.


# Test the function with multiple operations.


def calculator(num1, num2, ope):
    if ope == "+":
        return num1 + num2
    elif ope == "-":
        return num1 - num2
    elif ope == "*":
        return num1 * num2
    elif ope == "/":
        return num1 / num2

print(calculator(10, 5, "+"))
print(calculator(10, 5, "-"))
print(calculator(10, 5, "*"))
print(calculator(10, 5, "/"))


#------------------------------------------------------------
# Exercise 9: Palindrome Checker
# Write a function that checks if a string is a palindrome.


# # Test the function with different words.
# print("Is 'radar' a palindrome? {}".format(is_palindrome("radar")))
# print("Is 'hello' a palindrome? {}".format(is_palindrome("hello")))

def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

# word = input("Enter a word: ")

# if is_palindrome(word):
#     print(f"{word} is a palindrome")
# else:
#     print(f"{word} is not a palindrome")


# print("Is 'radar' a palindrome? {}".format(is_palindrome("radar")))
# print("Is 'hello' a palindrome? {}".format(is_palindrome("hello")))



#------------------------------------------------------------
# Exercise 10: Display Multiplication Table
# Write a function that takes a number and prints its multiplication table.

# Call the function with a number.
# multiplication_table(5)
5
def multiplication_table(num):
    for i in range(1,13):
        print(f"{i} x {num} = {i*num}")



num = int(input("Enter a number: "))

multiplication_table(num)



#------------------------------------------------------------