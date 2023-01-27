"""
Part 3 – Count Vowels
Create a file called CountVowels.py that returns the number of vowels in a given word.
The user should be able to input a word (as a string) and count the number of vowels (A,E,I,O,U) in said word.
"""


user_input = "Create a file called that returns the number of vowels in a given word."
def solve(user_input):
    result = []
    vowels = 0
    consonants = 0
    for i in user_input:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            vowels += 1
        else:
            consonants += 1
    result.append(vowels)
    result.append(consonants)
    return result
print(solve(user_input))


"""
Stretch goal – The user can enter 3 additional letters into the program that it will then check for, 
and return the total number of found letters. I.e the user enters B, P, T and also enters BURRITO, it should return 5 (B, U, I, T, O).
"""


