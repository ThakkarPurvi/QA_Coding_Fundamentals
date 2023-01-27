"""
Part 3 - Pythagoras
Create a program called Pythagoras.py that can return the long angled side of a right angled triangle. Pythagoras’ Theorem states
that the square of the long side (C) of a right-angled triangle is the sum of the squares of the two shorter sides (A and B).

The user should be able to implement the lengths of sides A and B to return the length of C.
"""

side = input("What side of the triangle do you want to know? (A, B or C):  ")
side1 = float(input("Side1: "))
side2 = float(input("Side2: "))
def pythagoras(side,side1,side2):
    if side == "A" or side == "B":
        length = (side1 ** 2 + side2 ** 2) ** (1/2)
    else:
        if side2 < side1:
            temp = side2
            side2 = side1
            side1 = temp
        length = (side2 ** 2 - side1 ** 2) ** (1/2)
    return length

pythagoras()



"""
Stretch goal – You should use an input statement to allow the user to choose which side to calculate (A, B or C) and run the correct sum.
"""
