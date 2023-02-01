""" A Class is a type of code that allows you to create objects.
    It dosent have to be same name as file and creates objects of type <cake>"""


"""
__init__ Acts as a constructor to create cake objects
__init__() Special function that is called initially when the class is running
layers, flavour, vegan, ingredients are all attribute 
self must be added and allows teh function to refer to the object. 
cake layers attribute is equal to 2 
"""
class cake:
    def __init__(self, layers, flavour, vegan, ingredients):
        self.layers = layers
        self.flavour = flavour
        self.vegan = vegan
        self.ingredients = ingredients

    def bake(self):
        return f"Almost finished cooking your {self.flavour} cake"

    def __str__(self):
        return f"flavour: {self.flavour}  layers: {self.layers}  ingredients: {self.ingredients}"

    def changeFlavour(self, newFlav):
        self.flavour = newFlav
        return True

""" Objects can also contain functions
    python class functions MUST include the word self
    self is referring to this specific object
    When printing any complex object (arrays, strings, cake) we run the __str__()
"""

cake1 = cake(2, "Vanilla", False, ["flour", "eggs", "milk"])
cake2 = cake(3, "Chocolate", True, ["Choc", "flour", "eggs", "milk"])
cake3 = cake(1, "Plain", False, ["flour", "eggs"])
cake4 = cake(5, "Raspberry", False, ["flour", "eggs"])

print("--------- Cake 1 ----------")
print(cake1)            # Output : <__main__.cake object at 0x0000014231590FD0>
print(cake1.flavour, cake1.vegan, cake1.ingredients)
print(cake1.bake())                     # we don't pass in a 'self' but self refers to the object we are running
# print(cake.bake()) - there is no 'self' for cake as it is a class, a static method

print(cake1.flavour)
print(cake1.ingredients)
print(cake1.layers)

print("--------- Cake 2 ----------")
print(cake2.__str__())
print(cake2)

cake1.changeFlavour("coffee") # using function to change to coffee
cake1.flavour = "raspberry"   # directly changing value
print(cake1)

""" getattr - returns the value of named attribute of object
    setattr - changes the value of named attribute
    delattr - deletes this attribute
    hasattr - checks if attribute is there and returns true or false """

print("*****************************************")

setattr(cake1, "flavour", "almond") # updates AND creates new attributes
print(cake1.flavour)

delattr(cake1, "candles")
print(hasattr(cake1, "candles")) # returns false
if hasattr(cake1, "candles"):
    print(getattr(cake1, "candles")) # cake has no attr called candles
else:
    print("Cake 1 has no candles :(")