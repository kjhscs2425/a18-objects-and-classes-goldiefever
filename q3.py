# -*- coding: utf-8 -*-

class Cat:
    """a cat"""
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return(f"<a cat named {self.name} 🐱")
    def speak(self):
        return(f"{self.name} says hi!!! 🐈")

# Write a new class `Dog`.
# Your class should have its own `__init__` method that sets a attribute `name`.
# Your class should have its own `__str__` method that returns a string.
#### YOUR CODE HERE ####
class Dog:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return(f"{self.name} is a dog!!! 🐩")
# Make a new object of class `Dog` and print it out
#### YOUR CODE HERE ####

nessie = Dog("Nessie")
print(nessie.__str__())




