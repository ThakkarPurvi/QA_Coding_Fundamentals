""" A class in Python is a blueprint for creating objects (instance of a class).
    A class defines a set of attributes and methods that are common to all objects of that type.
For example, you could define a "bird" class with
attributes such as species, color, and number of wings, and methods such as fly and tweet."""

print("------------- Showing Inheritance ------------------")

class bird:
    def __init__(self, species, color, wings, age):
        self.species = species
        self.color = color
        self.wings = wings
        self.age = age

    def sound(self):
        return "Tweet tweet."

class penguin(bird):
    def __init__(self, species, color, wings, age, swim):
        super().__init__(species, color, wings, age)
        self.swim = swim

    def swim(self):
        return "The penguin can swim."


class eagle(bird):
    def __init__(self, species, color, wings, age, fly):
        super().__init__(species, color, wings, age)
        self.fly = fly

    def can_fly(self):
        return "The bird can fly."

    def sound(self):
        return "Screeching"

p1 = penguin("King Penguin", "White", True, 20, True)
print(f"-" * 10,"\nPenguin\nSounds like:", p1.sound(), "\nAge:",p1.age, "\nCan swim:",p1.swim,"\n","-" * 15)


e1 = eagle("King Eagle", "Black", True, 35, True)
print(f"-" * 10,"\nEagle\nSounds like:", e1.sound(), "\nAge:",e1.age, "\nCan Fly:",e1.can_fly(),"\n","-" * 15)

print("------------- Showing abstract  ------------------")

from abc import ABC, abstractmethod

class abstract(ABC):
    @abstractmethod
    def move(self):
        pass

class human(abstract):
    def move(self):
        return "I can think"

class bird(abstract):
    def move(self):
        return "I can fly"

class animal(abstract):
    def move(self):
        return "I can walk and run"

class reptiles(abstract):
    def move(self):
        return "I can crawl"


h = human()
b = bird()
a = animal()
r = reptiles()

print(f"Human:", h.move(),"\nBird:", b.move(), "\nAnimal:", a.move(), "\nReptiles:", r.move())

print(f"---------- ENCAPSULATION ----------")

""" Encapsulation in object-oriented programming refers to the concept of wrapping data and functions within an object (such as a class), 
and providing restricted access to that data and functionality through methods defined in the class. 
This helps to protect the data and functions within the object from accidental or intentional modification, 
and makes it easier to maintain and modify the code."""

""" In this example, the data of the penguin (name, and weight) is stored as private instance variables (indicated by the double underscores in their names).
The methods get_name(), and get_weight() are used to access the values of these instance variables, 
while the methods set_name(), and set_weight() are used to modify them. 
This ensures that the data is protected from any code that exists outside of the class, and that the values can only be modified through these defined methods.  """


class Penguin:
    def __init__(self, name, weight):
        self._name = name
        self._weight = weight

    def get_name(self):
        return self._name

    def set_name(self, name):
        if name == "King":
            return "Invalid Name!"
        else:
            self._name = name


    def get_weight(self):
        return self._weight
blah blah
    def set_weight(self, weight):
        if weight <= 10:
            return "Invalid Weight!"
        else:
            self._weight = weight

p2 = Penguin("King", 20)

print(p2._name)
# print(p2.get_weight())
print(p2.set_weight(5))
# print(p2._weight)
