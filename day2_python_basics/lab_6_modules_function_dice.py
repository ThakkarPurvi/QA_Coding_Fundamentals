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
    for i in range(4):
        roll = []
        for j in range(6):
            num = random.randint(1, 6)
            roll.append(num)
        six_side_dice.append(roll)
    return six_side_dice
print(f"4 Dices of 6: ",four_dices_of_six())

"""
Write a function which rolls 4 six sided dice, removes the smallest number from the pool 
(2, 4, 3, 5: remove 2 from the pool and add 4 + 3 + 5). Keep track of this number and generate 6 of these dice values. """





"""
Stretch goal – Separate out the dice rolling function so that one function runs another so that each function 
only does one thing and is simplified. 
"""


