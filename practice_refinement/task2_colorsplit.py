# A text file shapes.txt stores a list of shapes with a comma between each value.  

# The current contents of shapes.txt are: 
# star,sphere,square,triangle 

# A text file colours.txt stores a list of colours with a comma between each value.  

# The current contents of colours.txt are: 
# red,yellow,green,blue 

# A program reads the data from each file and creates a dictionary of the values 
# so that each shape has an associated colour. The first value in each file 
# will be joined, for example, star and red. 


# The function read_values() reads the data from both files and stores 
# the data in the global dictionary data_stored.  

# The data from the shapes.txt file is used as the key and the data 
# from the colours.txt file is used as the value. 

# The function needs to work for files of any length. The files will 
# always have the same number of data values. 

# Return the dictionary data_stored

# Write program code for the function read_values(). 

# 1. open and read both colour and shapes files
# 2. use .split() to split colour into list
# 3. use .split() to split shapes into list
# 4. enter values into dictionary

def read_values():
    with open("shapes.txt", "r") as fobj:
        shapes = fobj.read()
        
    with open("colours.txt", "r") as fobj2:
        colour = fobj2.read()

    shapes_list = shapes.split(",")
    colour_list = colour.split(",")
    data_stored = {}

    for i in range(len(shapes_list)):
        data_stored[shapes_list[i]] = colour_list[i]

    return data_stored

    # print(shapes_list)
    # print(colour_list)  
    
shape_color = read_values()
print(shape_color)


## Part 2:
# Write a function called check_color()
# takes in a parameter called shape (string), and a parameter called shape_color (dictionary)
# the function will return the color for the shape
# if the shape does not exist in the dictionary, return None

def check_color(shape, shape_color):
    if shape in shape_color:
        color = shape_color[shape] #???

        return color

    else:
        return None #null value

# print(check_color("star",shape_color)) # red
# print(check_color("diamond",shape_color)) # None



# Part 3:
# write a program to ask the user to enter the shape
# call the check_color() function to return the color
#   example output: the color for star is red
# if the shape does not exist, it will print out an appropriate message
#   example output: diamond does not exist
# the program will ask again and again until the user chooses to stop the program

while True:
    shape = input("Enter a shape: ").lower()

    color = check_color(shape, shape_color)

    if color == None:
        print(f"{shape} does not exist")

    else:
        print(f"The colour for the {shape} is {color}")
        prompt = input("Do you want to continue?: type 'n' to stop: ").lower()

        if prompt == "n":
            break
        # elif prompt == "y":
        #     continue
        # else:
            