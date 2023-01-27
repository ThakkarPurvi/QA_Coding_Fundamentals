"""
Lab 4 – Lists
Task 1 – Working with large List
In this task you will be working with a set of numbers below: """

ages =[12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,79,64,78,37,3,8,68,22,4,60,33,82,45,
        23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25,63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]


# Record the length of the list of variables and save this as a variable
len_ages = len(ages)
print(len_ages)


# Display all of the numbers in the list line by line using some form of loop
ages =[12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,79,64,78,37,3,8,68,22,4,60,33,82,45,
        23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25,63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]

for i in ages:
    print(i)

# Looping through the list, increase the value of each age by 1

ages =[12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,79,64,78,37,3,8,68,22,4,60,33,82,45,
        23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25,63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]

for i in ages:
    if i == i:
        print(i + 1)

# Create a new list which only contains the ages in the age range of 16 – 65,
#   display the new list and confirm it only contains 16 – 65 year olds

ages =[12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,79,64,78,37,3,8,68,22,4,60,33,82,45,
        23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25,63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]

age_16_to_65 = []

for i in range(len(ages)):
    if i >= 16 or i > 65:
        age_16_to_65.append(i)
    if i >= 65:
        break
print(age_16_to_65)



# Display the count of 16 – 25 year olds in the new list

ages =[12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,79,64,78,37,3,8,68,22,4,60,33,82,45,
        23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25,63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]
age_16_to_25 = []

for i in range(len(ages)):
    if i >= 16 or i > 25:
        age_16_to_25.append(i)
    if i >= 25:
        break
print(age_16_to_25)
print(len(age_16_to_25))

# Sort the ages of the new list (hint use <list>.sort())




# What proportion of people belong in the 16 – 25 category within the new list """



