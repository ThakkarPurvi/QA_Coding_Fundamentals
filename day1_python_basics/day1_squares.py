""" Lab 3 – Iteration Lab
Task 1 – Using While Loops
Part 1 - Squares
Add a new file called Squares.py and add the following to it:
"""

number = 1
while number < 100:
    numberSqr = number * number
    print(numberSqr)
    number += 1


"""
When this code runs it prints the square of each number from 1 -100.
Add an if statement to end the loop if the square of a number is greater than 2000.
"""


number = 1
while number < 100:
    numberSqr = number * number
    print(numberSqr)
    number += 1
    if numberSqr >= 2000:
        break
