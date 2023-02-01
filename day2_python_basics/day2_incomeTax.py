"""
Task – Create a custom function to work out tax
Create a program called day2_incomeTax.py, this file will contain custom functions to work out the tax on an annual salary.
The user will be able to input in a salary and it would return the taxable amount of the salary.
This will be done in two parts with the simple version of tax which is total tax (simplified) and complex which is bracketed tax.

Tax breakdowns are below:
No tax paid on £12,570 personal allowance.
£12,571 to £23,000 starter rate of 19%
£23,000 to £40,000 intermediate rate of 30%
£40,001 to £150,000 higher rate of 41%
Above £150,000 top rate of 46%
Simple version: Entire Salary will be taxed to the bracket it belongs in
Complex version: With the salary it is taxed correctly with it being bracketed,
this should be done with a series of loops and conditional statements """


def total_tax_simplified():
    salary = int(input("What is your Salary?: "))
    if salary <= 12570:
        print("Your do not pay any tax.")
    elif salary >= 12571 and salary <= 23000:
        print("You will fall under starter rate of 19%.")
    elif salary >= 23001 and salary <= 40000:
        print("You will fall under intermediate rate of 30%.")
    elif salary >= 40001 and salary <= 150000:
        print("You will fall under higher rate of 41%.")
    elif salary > 150000:
        print("You will fall under top rate of 46%.")
# total_tax_simplified()

# 23000-12570

def bracketed_tax():
    salary = int(input("What is your Salary?: "))
    if salary <= 12570:
        print(f"Your do not pay any tax.")
    elif salary >= 12571 and salary <= 23000:
        print(f"You will fall under starter rate of 19%.\nYour tax amount is:",(salary-12570) * 19/100)
    elif salary >= 23001 and salary <= 40000:
        print("You will fall under intermediate rate of 30%.\nYour tax amount is:",(salary-12570) * 30/100)
    elif salary >= 40001 and salary <= 150000:
        print("You will fall under higher rate of 41%.\nYour tax amount is:",(salary-12570) * 41/100)
    elif salary > 150000:
        print("You will fall under top rate of 46%.\nYour tax amount is:",(salary-12570) * 46/100)
bracketed_tax()