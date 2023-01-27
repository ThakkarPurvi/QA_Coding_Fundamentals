""" For Loops - Used when you know exactly how many times the code should loop
    For loops work by doing x code block for every (item) in a list
    Range - function that generates a list of numbers with specific params """"

print(range(5))             # Makes a list of numbers from 0 - 5
print(*range(5))            # Inclusive (include num) of starting number (0), exclusive (stop before num) of ending number (5)
print(*range(11))           # 0 1 2 3.. 10

print(*range(2, 10))        # Start from 2, end at 10

print(*range(4, 30, 6))     # Start at 4, end at 30, increasing in 6's
print(*range(20, -7, -3))   # counting down

"""" for the list 0, 1, 2, 3, 4 .. 9 do the following code block
    and replace each element of the list with the variable num """

for num in range(10):
    print(num)

print("**************************")

for num in range(50, -42, -13):
    print(f"Value of num is {num}")

print("=============================")

colourList = ["red", "blue", "green", "purple"]

for zipZoop in colourList:
    print(zipZoop)


""" =================================== IN-BUILT FUNCTIONS ========================================================= 

import random

# Python Functions
# Inbuilt functions which are always accessible
# Package functions we can import from Python / pip
# Custom functions that we define ourselves

# Functions are ways of repeating a block of code when it is called
# Loops run continuously and you can't assign a whole 'loop' 

# Function can be defined with a name, and called by calling that name at any point in time 
"""

print("Sends this data to the terminal")

# Functions must be called, by defining the name then with ()
# A lot of python built in functions are focused around data types
# String functions, number functions

numbers = [19,63,51,7,99,11,23,15,17,8]

print(min(numbers)) # minimum number from an array
print(max(numbers)) # max from an array
print((pow(2,4)))


num1 = int(input("Please choose num 1: "))
num2 = random.randint(1, 6)
print(pow(num1, num2))


float = 5.624864635161
print(round(float, 2))

# Formatting strings
str = "hElLo \nWoRlD!!!!"
print(str)

# Typically numbers don't have functions, but are used in functions
# Numbers are 'simple' data types, booleans, chars (a, e, 1, +)
# String is a complex data type, it is an array of 'chars'

print(str.lower())
print(str.upper())
print(str.replace("!", ".."))
print(str.replace("!", ""))
print(len(str))
new_str = str.replace("\n", "")

print(new_str.center(40, "*"))

# Split function .csv file

cities = "london,birmingham,leeds,manchester,bristol"
print(cities[24:34])
city_list = cities.split(",")
print(city_list)
print(city_list)



""" =========================================== MODULES FUNCTIONS ===================================================

# Functions are ways we can 'repeat' blocks of code under specific conditions
# Functions should be used to handle the logic of your application 

# Global / non functional - code """

# print(
#     """
#         Welcome to QA Calculator!
#         Please select a choice from below:

#         1. Add
#         2. Subtract
#         3. Multiply
#         4. Divide
#         5. Power
#     """
# )

# choice = int(input("Please select a number between 1 and 5: "))
# num1 = int(input("Please select number 1: "))
# num2 = int(input("Please select number 2: "))

# if choice == 1:
#     print(num1 + num2)
# elif choice == 2:
#     print(num1 - num2)

# Functional code is when code is split into repeatable and callable modules

# def - define, defining the function we wish to use
# All functions can take in paramaters (when they are created)
# These are variable placeholders that are set when function is called


def addSum(x, y):
    total = x + y
    print(f"{x} + {y} = {total}")

# Calling the function
addSum(10, 15) # x = 10, y = 15

addSum("Hello", "World") # HelloWorld
# addSum("Hello", 5000)

# Typically all functions should 'return' something
# All functions should output something from the codeblock for external use

def subSum(x, y):
    total = x - y
    return total # return is the keyword, what is this function returning

result = subSum(45, 10) # if AddSum() output or returned something result would be equal to it
print(result)

# If your function doesn't need to return anything useful.. make it return True

# CallBack functions, we pass in a function as a paramater to a different function

def berryFunc(adjective):
    print("Berry func runs")
    berry = f"{adjective}berry"
    return berry

def berryCallback(function):
    print("Berry call back runs")
    return f"Delicious {function}"

# print(berryFunc("blue"))
print(berryCallback(berryFunc("red")))