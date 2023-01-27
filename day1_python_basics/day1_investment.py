"""
Part 2 - Investment
Create a file called Investment.py, this file should calculate how many years it will take an
initial investment of £100 to grow to a target value of £1000 if the interest rate is 10%.
This program should use while loops to achieve the result.
"""

year = 0
investment = 100
interest = "10 percent"
total = investment

while total <= investment * 2:
    total = total + total * (10) / 100
    year = year + 1

print(f"Number of no of years: {year}")



"""
Stretch goal – Make the program more usable by allowing the user to input values for: initial investment, 
target value and interest rate.
"""

year = 0
initial_investment = int(input("How much would you like to invest: "))
interest = int(input("What is the interest rate: "))
target_value = int(input("How much would you like to receive: "))

while target_value <= initial_investment * 2:
    target_value = target_value + target_value * interest / 100
    year += 1

print(f"Number of no of years: {year}")