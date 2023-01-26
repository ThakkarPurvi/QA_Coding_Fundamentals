"""
=======================================================================================
Part 1 – Create a python file and run it Using your editor of choice
Create a file called python-demo.py and add the following:
"""

print("Hello World")


"""
================================================================================================================================== 
You can then run your file via the run / execute command within your IDE or Editor or via the terminal with `python python-demo.py`
Task - Within your file print your top 3 favourite films on separate lines
"""

print("My 3 favourite movies are:\nPursuit of Happiness\nGod Father\nApollo 13")



"""
=======================================================================================
Part 2 – Using input fields and printing 
With python you can easily get user input and use it for other processes

"""

name = input("Please enter name: ")
print("Hello " + name)



"""
=========================================================================================================================
With this code it will save a variable called name as the text you enter and then print it adding “Hello “ in front of it.
Task – Write code that asks for user input for a coffee order, you should save variables for the following:
- name (text)
- drink type (text)
- whipped cream (Boolean)
- quantity (number)
Return a print statement which includes all of the info (‘Name: John Smith, drink: Mocha..’)
"""

name = input("Please enter name: ")
drink = input("Would you like Tea or Coffee?")
cream = bool(input("Would you like Whipped Cream on it?"))
quantity = int(input("How many would you like?"))

print("Your order is as below:\nName: ", name, "\nDrink: ", drink, "\nWhipped Cream: ", cream, "\nQuantity: ", quantity)




"""
=======================================================================================
Stretch goal – Also take in up to 3 values for extras, save this as an array
"""

name = input("Please enter name: ")
drink = input("Would you like Tea or Coffee?")
cream = bool(input("Would you like Whipped Cream on it?"))
cookies = input("Would you like to have Cookies?")
chips = input("Would you like to have chips?")
sandwiches = input("Would you like to have Sandwiches?")
quantity = int(input("How many would you like?"))

order = [drink, cookies, chips, sandwiches]
print("Your order is as below:\nName: ", name, "\nOrder: ", order, "\nWhipped Cream: ", cream, "\nQuantity: ", quantity)




"""
=======================================================================================
Lab 2 – Selection Lab
Task 1 – Using If Else control flow statements
Within a new python file add the following code: 
"""

age = int(input("Please enter age: "))
if age >= 18:
    print("You are in Cat A")

"""
=======================================================================================
Run the code with an age greater than 18 and see what the output is.
Develop on this code piece so it prints “You are in Cat B” when the age is equal to 16 and “You are in Cat C” when it is below 16.
Stretch goal – If you did not use If Else statements for the above snippet, convert it to If Else statements.
Task 2 – Use If Else for more complex commands"""


age = int(input("Please enter age: "))
if age <= 2:
    print("You are Baby")
elif age >= 2 and age <= 12:
    print("You are a Child")
elif age >= 13 and age <= 17:
    print("You are a Teenager or a Young person")
elif age >= 18 and age <= 65:
    print("You are an Adult")
else:
    print("You are an Elderly person")

