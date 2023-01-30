"""
Create a file containing, fav animals , use python to loop through each animal.
"""

animal_file = open("./day3_animals.txt")
print(animal_file) # Not useful data
data = animal_file.readlines() # get data from file
print(data)

for a in data:
    print(a)

animal_file.close()


"""
Stretch Goal: Modify the strings so they dont have a \n
"""

for j in data:
    print(j.replace('\n', ''))
animal_file.close()

"""
Lab 7 – File IO
Task – Write and Read Data from a basic .txt file
Within your working directory create a python file called FileIO.py and a fruit.txt file. Within the fruit.txt file add a string of 5 fruit separated by commas “apples, pears, bananas”. 
Within the python file add the following """

# fruitFile = open("fruit.txt", "r")
# data = fruitFile.readline()
# print(data)
# fruitFile.close()

"""
When you run the code it will print the contents of the files. 
Task - Use inbuilt functions, lists and loops to print out each fruit line by line. 
The following code will append a new fruit to the file: 
Check the file to see the fruit.txt has the new fruit added. 
"""

# fruitFile = open("fruit.txt", "a")
# fruitFile.write("kiwi")
# fruitFile.close()



colour_file = open("./day3_colors.txt")
colour_data = colour_file.readlines()
print(colour_data)


for c in colour_data:
    print(c.split(',', '\n'))
colour_file.close()


"""
Task – Using a provided file, pull the data from it and manipulate
You will be provided a .csv file that contains Car Data showing sales of different companies across different months / years.
From this .csv you should extract the data, convert it to a series of lists and work out the following: 


1) Sum of cars sold by Ford in total
2) Sum of card sold in May 2019
3) Average of cars sold in Aug 2019
4) Car manufacturer who sold most cars Jan 2019 – Apr 2019
5) Month where the least amount of cars were sold
"""

