import statistics


class student:
    def __init__(self, name, age, group, subject, score, status):
        self.name = name
        self.age = age
        self.group = group
        self.subject = subject
        self.score = score
        self.status = status

    def average_score(self):
        return statistics.mean(self.score)


    def __str__(self):
        key, val = self.subject.items()[0]
        return f"Subject Name: {self.subject.items(key)},  Score: {self.subject.items[value]}"

    def change_name(self, new_name):
        self.name = new_name
        return True

S1 = student("Andre Smith", 20, "A", {"Maths": 70, "English": 97, "Spanish": 85, "Music": 45, "History": 89}, [70, 5, 89, 86, 90], True)
S2 = student("Joe John", 22, "B", ["Maths", "English", "German", "Geography", "History"], [70, 50, 25, 96, 90], True)
S3 = student("Andrew Cooke", 20, "A", ["Maths", "English", "German", "Geography", "History"], [70, 50, 80, 56, 90], True)

print(S1.name, S1.age, S1.average_score())
print(S2.name, S2.age, S2.average_score())
print(S3.name, S3.age, S3.average_score())

print(f"Average score of", S3.name,"is:", S3.average_score())
print(f"Total score of", S2.name,"is:", S2.average_score())

print(S1.__str__())
print(S1)


print("------------------")

setattr(S1, "Andre")           # updates AND creates new attributes
print(S1.name)

delattr(S1, "Smith")
print(hasattr(S1, "Smith"))     # returns false
if hasattr(S1, "Smith"):
    print(getattr(S1, "Smith"))     # Student has no attr called Smith
else:
    print("Student 1 has no Smith: ")