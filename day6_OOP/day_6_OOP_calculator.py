""" Using previous code (calculator, print menu and functions for sums +, -, *, /, raise power)
    Ensure it is functional code (using functions where appropriate)

    Convert it to atleast two objects that interact with eachother
    1) Calculator Object running sums
    2) Printing object which prints what calculator returns """


class calculator:

    def __init__(self, brand):
        self.brand = brand
        print(f"*"*43,"\nWelcome to CASIO Calculator")

    def add_num(self, x, y):
        return x + y

    def subtract_num(self, x, y):
        return x - y

    def multiply_num(self, x, y):
        return x * y

    def divide_num(self, x, y):
        return x / y

    def square_num(self, x):
        return x * x

    def power_num(self, x, y):
        return x ** y


class calculate:

    def __init__(self, calculator):
        self.calc = calculator

    def getBrand(self):
        return self.calc.brand

    def menu(self):
        print(f"Please look at our Calculator Menu below:\n","*" * 43,
              "\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Square\n6. Power\n", "*" * 43)
        print("Type the number operator (.e.g. 1 for Add).")
        operator = int(input("Operator of your choice: "))
        if operator in (1, 2, 3, 4, 5, 6):
            print("Choose a number below: ")
            x = int(input("No 1: "))
            y = int(input("No 2: "))

            if operator == 1:
                print(f"Addition of", x, "+", y, "=", self.calc.add_num(x, y))
            elif operator == 2:
                print(f"Subtraction of", x, "-", y, "=", self.calc.subtract_num(x, y))
            elif operator == 3:
                print(f"Multiplication of", x, "*", y, "=", self.calc.multiply_num(x, y))
            elif operator == 4:
                print(f"Division of", x, "/", y, "=", self.calc.divide_num(x, y))
            elif operator == 5:
                print(f"Square of", x, "*", x, "=", self.calc.square_num(x))
            elif operator == 6:
                print(f"Power of", x, "**", y, "=", self.calc.power_num(x, y))



num_1 = calculator("CASIO")
cont1 = calculate(num_1)

cont1.menu()
print(cont1.getBrand())


print(f"*"*34,"\nThank you for using CASIO Calculator\n","*"*34)