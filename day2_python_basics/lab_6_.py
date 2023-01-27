"""
Lab 6 – Custom Functions
Task 1 – Basic Functions
Create a file called DiceRoller.py and add the following:
 When this function runs it returns a random number between 1 and 6. """

import random

def rollSix6():
    return random.randint(1, 6)
print(f"Dice of 6: ",rollSix6())

"""
Create 3 more functions that roll an eight sided dice, 
10 sided dice and 4 six sided dice. Run these functions separately and print their results.
You can enter a parameter into a functions’ () so that it passes the value in. This can be done to allow you to specify what 
size dice without needing to create multiple functions:
"""

def rollDice8():
    return random.randint(1, 8)
print(f"Dice of 8: ",rollDice8())

def rollDice10():
    return random.randint(1, 10)

print(f"Dice of 10: ",rollDice10())


import random
six_side_dice = []
roll = []
def four_dices_of_six():
    for i in range(6):
        roll = []
        for j in range(4):
            num = random.randint(1, 6)
            roll.append(num)
        six_side_dice.append(roll)
        return six_side_dice
print(f"4 Dices of 6: ",four_dices_of_six)

"""
Write a function which rolls 4 six sided dice, removes the smallest number from the pool 
(2, 4, 3, 5: remove 2 from the pool and add 4 + 3 + 5). Keep track of this number and generate 6 of these dice values. """




"""
Stretch goal – Separate out the dice rolling function so that one function runs another so that each function 
only does one thing and is simplified. 
"""


"""
Task – Create a custom function to work out tax
Create a program called incomeTax.py, this file will contain custom functions to work out the tax on an annual salary. The user will be able to input in a salary and it would return the taxable amount of the salary. This will be done in two parts with the simple version of tax which is total tax (simplified) and complex which is bracketed tax. 

Tax breakdowns are below:
No tax paid on £12,570 personal allowance.
£12,571 to £23,000 starter rate of 19%
£23,000 to £40,000 intermediate rate of 30%
£40,001 to £150,000 higher rate of 41%
Above £150,000 top rate of 46%
Simple version: Entire Salary will be taxed to the bracket it belongs in
Complex version: With the salary it is taxed correctly with it being bracketed, 
this should be done with a series of loops and conditional statements """