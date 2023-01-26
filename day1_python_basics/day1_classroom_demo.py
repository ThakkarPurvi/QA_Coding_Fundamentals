"""
Python is a dynamically typed scripting language
In ANY languages (that support comments), these lines are not read by an interpreter
Used for information to other devs

Dynamically typed
Variable is a placeholder of data the variable called name is a String
String name = "app"
"""

name = "app"        # At the minute this is a STRING
name = 123          # The type of variable is dynamically read by the interpreter and can change

print(name)         # Outputs the content in the () to the terminal, so we can read it



""" Python is primarily a scripting language that 'typically' reads a file from top to bottom """
print(5)
print(1)
print(2)
print("Hello world")


""" Python is dynamically typed meaning you don't need to explicitly specify type """
string = "Red"
boolean = True   # True or False
int = 123
float = 1.23

print(boolean)
print(int)
print(float)
print(string)


""" Arrays, collect data - tuples, lists, dictionaries, sets """
favFruits = ["Mango", "Kiwi", "Banana"]     # List
print(favFruits)        # array.atObject <efef83e93038fef>


""" Naming conventions and best practice
variable names should only contain abcABC123 _ $
percentage% = 30
last name = "no spaces allowed"
money$ = 1234
print = "a4 paper"
GLOBAL_VARS = "ALL UPPERCASE AND _"
camelCase = "my favourite"
snake_case = "not my fav"
PascalCase = "another type" """

# Inputs - Allow the user (us) to enter data into our python code
# Python is typically a language designed for Devs to use to help with other tools

favColour = input("Please enter your fav colour: ")
print("my fav colour is " + favColour)          # String concatenation, adding multiple strings together


""" ===========================================================================
 Selection / Conditionals
 - Selection lets us specify what our code should do under certain conditions
 - All logic is binary, it either does something or doesn't
"""

check = True        # True is a boolean, the opposite is false


""" - When using == we are checking for values
    - When using = we are  this """

if check == True:
    print("check is true")
else:
    print("Check is not true)")

points = int(input("Enter a points number: "))          # points = "five"

if points < 5:
    print("Points less than 5")
elif points > 5:
    print("Points is greater than 5")
else:
    print("Points equal to 5")



""" What do we know if points is not less than 5 """

print("===========================================")
colour = "Red"
# use string.lower() or .upper() tio convert to different cases for validation
if colour.lower() == "red":
    print("colour is red")
else:
    print("Colour is not red")

cakeSize = 20
frosting = False

""" 
Complex conditional statement with multiple conditions
 OR  - if condition 1 is true or condition 2 is true or both are true
 AND - if cond 1 is true AND cond 2 is true
"""

if frosting == False and cakeSize > 21:
    print("Frosting is false AND cake is bigger than 21")
elif frosting == True:
    print("Frosting is true")
elif cakeSize > 21:
    print("Cake is bigger than 21")
else:
    print("Cake is smaller than 21 and frosting is false")

if frosting == False or cakeSize > 21:
    print("either frosting is false, or cakesize is bigger than 21, or they are both true")
    if frosting or colour == "red":
        print("Cake size is bigger than 21 ")
    if not frosting:
        print("Cake is not frosted")

""" When checking a boolean for True or False we can just put in the boolean we're checking
    Only works this way for True booleans
"""

