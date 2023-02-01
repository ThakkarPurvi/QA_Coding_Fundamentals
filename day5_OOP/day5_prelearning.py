"""
Object Oriented Programming (OOP) has four key principles:

    Inheritance - One object acquires all the properties and behaviours of a parent object.
    Polymorphism - Performing a single action in different ways.
    Abstraction - Hiding the implementation details so that the user can only see the functionality.
    Encapsulation - Wrapping code and data together into a single unit for data integrity.

We can use these principles to define complex types, known as classes.
Classes are a set of attributes (data) and methods (code) that you can use to create objects,
which are usable instances of classes that you can operate on.
"""


""" Create a Student class that takes the name and age on creation.
    Create two objects of your student class and get the age of one of them. """

print(" =========== Student class with name and age ============")
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Andre Smith", 30)
student2 = Student("Joe John", 42)

print(student1.name, "is", student1.age,"years old")
print(student1.name, "is", student2.age,"years old")


print(" =========== Student class with avg test scores ============")

class Student:
    def __init__(self, name, age, current_class):
        self.name = name
        self.age = age
        self.current_class = current_class

    def average_test_score(self, test1, test2, test3):
        return (test1 + test2 + test3) / 3

student1 = Student("Andre Smith", 20, "Class A")
student2 = Student("Joe John", 22, "Class B")

average_score = round(student1.average_test_score(70, 65, 70))
print(f"Average score of", student1.name,"is:", average_score)

""" Create three classes: a Bird parent class and then an Owl and Dodo class.
    Make use of the four OOP principles """

print(" =========== Bird parent class, an Owl and Dodo class ============")
# Parent Class: Bird
class Bird:
    def __init__(self, species, feathers, wingspan):
        self.__species = species
        self.__feathers = feathers
        self.__wingspan = wingspan

    def fly(self):
        return "Flapping wings"

    def get_species(self):                  # GET
        return self.__species

    def set_species(self, species):         # SET
        self.__species = species

    def get_feathers(self):                 # GET
        return self.__feathers

    def set_feathers(self, feathers):        # SET
        self.__feathers = feathers

    def get_wingspan(self):                  # GET
        return self.__wingspan

    def set_wingspan(self, wingspan):         # SET
        self.__wingspan = wingspan


# Child Class: Owl
class Owl(Bird):                                    # OWL Class
    def __init__(self, species, feathers, wingspan, nocturnal):
        Bird.__init__(self, species, feathers, wingspan)
        self.__nocturnal = nocturnal

    def fly(self):
        return "Gliding silently"

    def get_nocturnal(self):                        # GET
        return self.__nocturnal

    def set_nocturnal(self, nocturnal):             # SET
        self.__nocturnal = nocturnal


# Child Class: Dodo
class Dodo(Bird):                                   # Class Dodo
    def __init__(self, species, feathers, wingspan, extinct):
        Bird.__init__(self, species, feathers, wingspan)
        self.__extinct = extinct

    def fly(self):
        return "Can't fly, can only waddle"

    def get_extinct(self):                      # GET
        return self.__extinct

    def set_extinct(self, extinct):             # SET
        self.__extinct = extinct


print("--- Inheritance ---")
owl = Owl("Owl species", "Soft feathers", 2, True)
print("Owl species:", owl.get_species())
print("Owl feathers:", owl.get_feathers())
print("Owl wingspan:", owl.get_wingspan())
print("Owl flight:", owl.fly())
print("Owl nocturnal:", owl.get_nocturnal())

print("--- Encapsulation ---")
owl.set_species("Owl species 2")
print("Owl species:", owl.get_species())

print("--- Polymorphism ---")
dodo = Dodo("Dodo species", "Thick feathers", 1, True)
print("Dodo species:", dodo.get_species())
print("Dodo feathers:", dodo.get_feathers())
print("Dodo wingspan:", dodo.get_wingspan())
print("Dodo flight:", dodo.fly())
print("Dodo extinct:", dodo.get_extinct())

print("--- Abstraction ---")
birds = [owl, dodo]
for bird in birds:
    print(bird.fly())
    print(bird.get_feathers())
