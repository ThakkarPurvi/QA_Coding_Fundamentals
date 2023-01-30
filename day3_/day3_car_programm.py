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

print("""" ==================== OPEN AND VIEW FILE IN CONSOLE ========================== """)
file = open("./cars.csv")
read = file.readlines() # get data from file
print(read)
print("\n")
for a in read:
    print(a)
file.close()

print("""" ==================== Sum of cars sold by Ford in total ========================== """)
import csv

with open('./cars.csv') as f:
    reader = csv.reader(f)
    month_tup = [tuple[row1] for row1 in reader]
    # ford = [tuple(row2) for row2 in reader]
print(f"Tuple:", month_tup)



print("======= MONTH =======")
month = read[0].split(",")
print(f"Month:",month)

print("===== Ford =======")
ford = read[1].split(",")
print(ford)

print("===== Volkswagen =======")
volkswagen = read[2].split(",")
print(volkswagen)

print("===== Mercedes =======")
mercedes = read[3].split(",")
print(mercedes)

print("===== Vauxhall =======")
vauxhall = read[4].split(",")
print(vauxhall)

print("===== BMW =======")
bmw = read[5].split(",")
print(bmw)

print("========= FORD STRING TO INT =========")
ford_nums = []
counter = 0
for f in ford:
    if counter != 0:
        new_data = f.replace('"',"")
        ford_nums.append(int(new_data)) # Adding clean data to array
    counter += 1
print(f"Ford Numbers:", ford_nums)

# print("========== FORD STRING TO INT =============")
#
# for i in range(0, len(ford_nums)):
#     ford_nums[i] = int(ford_nums[i])
# print("Modified list is: " + str(ford_nums))

print("========== FORD SUM =============")
ford_total = sum(ford_nums)
print(f"Total Sales for Ford: ", ford_total)

print("========== Sum of card sold in May 2019 =============")

may_nums = []
counter = 0
for m in month_tup:
    if counter != 0:
        may_data = f.replace('"',"")
        may_nums.append(int(may_data)) # Adding clean data to array
    counter += 1
print(f"May Numbers:", may_nums)


print("========== Average of cars sold in Aug 2019 =============")
print("========== Car manufacturer who sold most cars Jan 2019 – Apr 2019 =============")
print("========== Month where the least amount of cars were sold =============")