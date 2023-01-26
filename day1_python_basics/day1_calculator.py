"""
Part 1 - Calculator
Create a program called Calculator.py that lets the user choose what command out of the following
Add, Subtract, Multiply, Divide, Raise To Power they wish to do, to two numbers that are entered by the user.
Your file should first print out a menu like the below:

Add
Subtract
Multiply
Divide
Power

Using an input statement to choose a number between 1 – 5, and then asking the user to input two numbers to plug into the command.
The program should print the sum and result i.e. if the user chooses to add and enters 4, 5 it should return 9.
"""

print(f"*"*43,"\nPlease look at our Calculator Menu below:\n","*"*43,"\n 1. Add\n 2. Subtract\n 3. Multiply\n 4. Divide\n 5. Power\n","*"*43)
print("Type the number operator (.e.g. 1 for Add) you want to execute from the calculator menu.")
operator = int(input("Operator of your choice: "))

if operator in (1, 2, 3, 4, 5):
    print("Choose a number between 1 – 5.")
    number1 = int(input("No 1: "))
    number2 = int(input("No 2: "))
    if operator == 1:
        print(number1, "+", number2, "=", (number1 + number2))
    elif operator == 2:
        print(number1, "-", number2, "=", (number1 - number2))
    elif operator == 3:
        print(number1, "*", number2, "=", (number1 * number2))
    elif operator == 4:
        print(number1, "/", number2, "=", (number1 / number2))
    elif operator == 5:
        print(number1, "**", number2, "=", (number1 ** number2))

print(f"*"*34,"\nThank you for using the Calculator\n","*"*34)
