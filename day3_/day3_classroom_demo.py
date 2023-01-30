""" Python is a good as a tool to help devs do everyday jobs,
    Useful tool for people who aren't specifically technical, data scientists, accountants, engineers
    Python is a good tool at reading and manipulating any form of 'data'
"""

# Using python we can access and print the contents of our .txt file
# important you are running the file from a directory that can see the .txt
fruit_file = open("fruit.txt")

print(fruit_file) # Not useful data

data = fruit_file.readlines() # get data from file

# print(data[0])
# print(data[1])
# print(data[2])
print(data)

for fruit in data:
    print(fruit)

fruit_file.close() # close the file so we can't make changes / something else can change it


# Exercise - Create a txt file containing favourite animals, use python to loop through and print each

# When opening files the default is 'read'
colours_file = open("colours.txt", "r")
colour_data = colours_file.readline()
print(colour_data)

# readline() reads the line we're currently on and converts it to a String
# readlines() reads ALL the lines, saves each as a string and creates a list of the strings

colour_list = colour_data.split(",")
print(colour_list)

for colour in colour_list:
    print(colour)

""" Writing / appending
    Writing = Replacing and updating the content of a file
    Appending = adding new stuff to the end  
    When writing to a file you can create a new file by specifying a file that doesn't exist """

file = open("newFile.txt", "w")

for x in range(10):
    newLine = f"Line number: {x + 5}\n"
    file.write(newLine) # Add this string to my file

file.close()

import random

file = open("appendFile.txt", "a")
file.write(f"This will be appended! random number: {random.randint(1, 30)}\n")
file.close()