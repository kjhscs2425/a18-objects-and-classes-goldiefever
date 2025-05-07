# -*- coding: utf-8 -*-

class Cat:
    """a cat"""
    def __init__(self, name):
        self.name = name
    def speak(self):
        # I'm being cute with the emoji here. Delete it if you get errors.
        return(f"{self.name} says meow!🐱")

ella = Cat("Ella")
ella.speak()
zoe = Cat("Zoe")
zoe.speak()

# Write a new class `Dog`.
# Your class should have its own `__init__` method that sets a attribute `name`.
# Your class should have its own `speak` method that uses its name.
#### YOUR CODE HERE ####
class Dog:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return(f"Hello! My name is {self.name}. Bark 🐶")


# Make a new object of class `Dog` and call its `speak` method
#### YOUR CODE HERE ####

nessie = Dog("Nessie")
nessie.speak()