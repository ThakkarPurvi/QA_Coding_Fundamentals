"""
Part 3 – Factorials
Add a file called Factorials.py that returns the factorial of an entered number.
The factorial is the number gained when multiplying all integers between 1 and the chosen number.
I.e Factorial of 4: 1 * 2 * 3 * 4  = 24. Use a For loop or While loop to achieve this
"""


num = 4
factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print(f"The factorial of", num, "is:",factorial)
