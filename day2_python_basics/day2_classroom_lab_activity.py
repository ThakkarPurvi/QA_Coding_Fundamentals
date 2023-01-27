"""
Task 2 – Using For Loops
Part 1 – Counting Down
Add a new file called CountingDown.py and add the following:
"""

for number in range(31, 0, -3):
    print(number)

""" This file will start from 31 and count down to 0, printing the result in each time. 
Develop this code so that it prints “This is less than 10” when the number is less than 10. 
The for loop should end after the first time “This is less than 10” has been printed. """

for number in range(31, 10, -3):
    print(number)
print("This is less than 10")
