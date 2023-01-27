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



"""
Part 3 – Factorials
Add a file called Factorials.py that returns the factorial of an entered number. The factorial is the number gained when multiplying all integers between 1 and the chosen number. I.e Factorial of 4: 1 * 2 * 3 * 4  = 24
Use a For loop or While loop to achieve this
"""

"""
Lab 4 – Lists
Task 1 – Working with large List
In this task you will be working with a set of numbers below:
ages =[12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,79,64,78,37,3,8,68,22,4,60,33,82,45,23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25,63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]
Record the length of the list of variables and save this as a variable
Display all of the numbers in the list line by line using some form of loop
Looping through the list, increase the value of each age by 1
Create a new list which only contains the ages in the age range of 16 – 65, display the new list and confirm it only contains 16 – 65 year olds
Display the count of 16 – 25 year olds in the new list
Sort the ages of the new list (hint use <list>.sort())
What proportion of people belong in the 16 – 25 category within the new list
"""

"""
Task 2 – Counting Vowels with a list
We will be developing our count vowels program created in the previous set of labs but using a list instead. 
"""


"""
The user should be able to input a string and use this string (which is a list of chars) to count the number of vowels directly. 
Stretch goal – The user can enter 3 extra letters and check if they are in the word. 
"""