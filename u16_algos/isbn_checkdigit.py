# Each book is assigned a id of 10 digits. First 9 is the book's ISBN, 
# while the last digit is used to validate the ISBN,

# 1. Multiply the first digit by 10, the second digit by 9, 
#    the third digit by 8, and so on, up to the ninth digit multiplied by 2. ### how to do this
# 2. Add up the products from step 1
# 3. Take the sum from step 2 modulo 11 
# 4. Subtract the result from step 3 from 11. if the result is 11, the check digit is 0. 
#    If the result is 10, the check digit is X (i.e. Roman numeral 10). 
#    Otherwise, the check digit is the result from step 4

# Test with these
# 1541675126
# 9810185073
# 981018509X
# 9812042539
# 9810157290

# (1) check_isbn() function
# Write a function called check_isbn() that takes in book_id (int) as a parameter
# and validates the ISBN by checking if the 
# last digit is correct. The function must return True if its valid, and False if invalid

def check_isbn(book_id):
    # 1541675126
    count = 10
    total = 0

    for i in book_id:
        if count > 1:
            temp = int(i) * count 
            count -= 1
            total += temp

    temp2 = total % 11
    result = 11 - temp2

    if result == 10:
        result = "X"

    if book_id[-1] == str(result):
        return True
    else:
        return False


# def check_isbn(book_id):
    # loop through the characters in book_id
    #   step 1: apply the multiplication 9,8,7,6,5,4,3,2.... but how??
    #   step 2: add the total
    #   step 3: total mod 11
    #   step 4: 11 - step_3 = output
    #           if output == 10, then output = X
print(check_isbn("1541645126"))
print(check_isbn("981018509X"))
print(check_isbn("9810157290"))
print(check_isbn("456434890X"))



# (2) main program

# You have been given a file containing ISBNs called list_isbn.txt
# the ISBNs are stored in the file with a "," separating one isbn from the next.
# e.g. "1541675126,9810185073,981018509X,9812042539,9810157290"
# a. Use the function check_isbn() to check if each value is a valid isbn

# b. store the result of the check into a list called list_isbn_check

# c. output the results of the check into a file called output_isbn.txt
#    the output may look like this "true,false,true"
    