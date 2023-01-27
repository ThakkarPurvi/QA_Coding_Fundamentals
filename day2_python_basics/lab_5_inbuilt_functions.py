"""
Lab 5 – Inbuilt Functions
Your task is using the Python inbuilt functions to read, manipulate and display students’ grades from a String.
The data to use is below:
"""

data= "100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"


# Create a new file called grades.py and go through the following steps:
# Convert the string into a list of values, this can be done through split()

new_data = data.split(",")
print(f"List separated using ,:", new_data)

# Display the minimum and maximum value of grades

data_int = []                     # arrary of string
for i in new_data:
    data_int.append(int(i))

print(f"Min:",min(data_int))
print(f"Max:",max(data_int))

# If your code displayed 100 as minimum and 99 as maximum work out why it has done this
# (hint – Are the values Strings or numbers?)


# Display the average of grades to 2 decimal points

avg = sum(data_int)/(len(data_int))
print(f"Average is:",round(float(avg)))


"""
# Import the statistics library using - `import statistics`
"""

import statistics

data = [100,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83]

print(f"Mean:",statistics.mean(data))
print(f"Mode:",statistics.mode(data))
print(f"Standard Deviation:",round(statistics.stdev(data)))



# Use the statistics.mean() function to get the average grade to 2 decimal points
avg_data = sum(data)/(len(data))
print(f"Average:",round(float(avg_data)))


# Display the median() value of this list
print(f"Median:",statistics.median(data))


# Use the string.format() to display the min, max, average, mean and median values
print("*"*60)
print(f"Min:",min(data), "Max:",max(data),"Average:",(round(float(avg_data))),"Median:",statistics.median(data),"Mean:",statistics.mean(data),"Mode:",statistics.mode(data))
print("*"*60)
