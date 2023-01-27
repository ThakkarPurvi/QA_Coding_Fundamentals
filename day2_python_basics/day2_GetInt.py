"""
Part 2 – Integer Between two limits
Add a file called GetInt.py that asks the user to input an integer between set minimum and maximum values (10, 40).
The user has 3 chances to guess the correct number, if they guess correct it returns “Correct!”,
if its wrong it says “Wrong.. guess again..” and they are given 3 guesses before it returns “Game Over.”
"""

# with While loop

run = True
while run:
    num = int(input("Add integer between these values (10, 40): "))
    if num == 25:
        print('You won!')
        run = False
    else:
        print("Wrong guess. Try again..")
        continue


# with for loop


count = 3
for i in range(3):
    num = int(input("Add integer between these values (10, 40): "))
    if num == 25:
        print('You won!')
        break
    else:
        print(f"Wrong guess. Try again! {count} left.")
        count -= 1
        continue
print("Game Over")

"""
Stretch goal 
The user is able to input different values for min and max values as well as the amount of guesses. 
"""


for i in range(50):
    print("Add integer between these values (10, 40)")
    min_no = int(input("Min from (10, 40): "))
    max_no = int(input("Max from (10, 40): "))
    if min_no == 12 and max_no == 34:
        print('You won!')
        break
    else:
        print(f"Wrong guess. Try again!")
        continue
print("Game Over")



"""
Stretch goal 2 
The program tells the user if the guess is cold or hot depending on how close they are, up to you how you implement this.
"""
