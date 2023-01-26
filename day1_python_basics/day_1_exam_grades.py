"""
Part 2 – Exam Grades
Create a program called ExamGrades.py that takes in a number between 1 and 100 and returns a Fail if less than 50,
Pass if between 50 and 60, Merit if between 60 and 70 and Distinction if above.

Stretch 1 – Add a check to ensure the grade is above 0 and below 100, if it’s not return an error statement.
"""

print(f"*"*30,"\n Welcome to the Score Board:\n","*"*30)
print("\nType your marks to check your Grades (marks between 1 - 100).")
marks = int(input("Marks: "))

if marks >= 0 and marks <= 100:
    if marks < 50:
       print("\nYou have failed the exams.\n")
    elif marks >= 50 and marks <= 60:
        print("\nCongratulation!!!! You have passed the exams.\n")
    elif marks >= 60 and marks <= 70:
        print("\nAwesome!!!! You have scored a Merit.\n")
    elif marks >= 18 and marks <= 65:
        print("\nMind Blowing!!!! You have scored a Distinction.\n")
else:
    print("\nIncorrect Type correct marks between 1 - 100")
    marks = int(input("Marks: "))
    if marks < 50:
        print("\nYou have failed the exams.\n")
    elif marks >= 50 and marks <= 60:
        print("\nCongratulation!!!! You have passed the exams.\n")
    elif marks >= 60 and marks <= 70:
        print("\nAwesome!!!! You have scored a Merit.\n")
    elif marks >= 18 and marks <= 65:
        print("\nMind Blowing!!!! You have scored a Distinction.\n")

print(f"*"*34,"\nThank you for checking your Grades\n","*"*34)




"""
Stretch 2 – Ask the user to input a choice between Level 1 and Level 2. If Level 1 is chosen the grade boundaries are the same,
if its Level 2 a Fail is less than 40, Pass is between 40 and 50, Merit is between 50 and 65, Distinction is above.
"""


print(f"*"*30,"\n Welcome to the Score Board:\n","*"*30)
print("\nType your Level to check your Grades (Level 1 or Level 2).")
level = int(input("Level: "))
marks = int(input("Marks: "))

if level == 1:
    if marks < 50:
       print("\nYou have failed the exams.\n")
    elif marks >= 50 and marks <= 60:
        print("\nCongratulation!!!! You have passed the exams.\n")
    elif marks >= 60 and marks <= 70:
        print("\nAwesome!!!! You have scored a Merit.\n")
    elif marks >= 18 and marks <= 65:
        print("\nMind Blowing!!!! You have scored a Distinction.\n")
else:
    if marks < 40:
        print("\nYou have failed the exams.\n")
    elif marks >= 40 and marks <= 50:
        print("\nCongratulation!!!! You have passed the exams.\n")
    elif marks >= 50 and marks <= 65:
        print("\nAwesome!!!! You have scored a Merit.\n")
    elif marks > 65:
        print("\nMind Blowing!!!! You have scored a Distinction.\n")

print(f"*"*34,"\nThank you for checking your Grades\n","*"*34)
