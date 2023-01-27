""" For Loops - Used when you know exactly how many times the code should loop
    For loops work by doing x code block for every (item) in a list
    Range - function that generates a list of numbers with specific params """"

print(range(5))             # Makes a list of numbers from 0 - 5
print(*range(5))            # Inclusive (include num) of starting number (0), exclusive (stop before num) of ending number (5)
print(*range(11))           # 0 1 2 3.. 10

print(*range(2, 10))        # Start from 2, end at 10

print(*range(4, 30, 6))     # Start at 4, end at 30, increasing in 6's
print(*range(20, -7, -3))   # counting down

"""" for the list 0, 1, 2, 3, 4 .. 9 do the following code block
    and replace each element of the list with the variable num """

for num in range(10):
    print(num)

print("**************************")

for num in range(50, -42, -13):
    print(f"Value of num is {num}")

print("=============================")

colourList = ["red", "blue", "green", "purple"]

for zipZoop in colourList:
    print(zipZoop)