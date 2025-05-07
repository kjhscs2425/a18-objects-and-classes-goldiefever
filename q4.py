# -*- coding: utf-8 -*-
import turtle
turtle.penup()
turtle.hideturtle()
turtle.pensize=5

# Write a new class `Point` with these methods:
# `__init__` sets `self.x` and `self.y`.
# `__str__` returns "(x, y)" for your object's x- and y-coordinates.
# `draw`:
#    1. uses `turtle.goto` to go to that x and y coordinate
#    2. stamps a point with `turtle.dot`



class Point:
    def __init__(self, x, y,):
        self.x = x
        self.y = y
    def __str__(self):
        return(f"{self.x,self.y}")
    def draw(self, emoji):
        turtle.goto(self.x,self.y)
        turtle.dot()
        turtle.write(self.__str__() + (f"{emoji}"), font = 8)

# Make 4 new objects of the class Point: (0, 0), (100, 0), (100, 100), (0, 100)
# Print your objects.
# Run your draw method for that object.

zero_zero = Point(0,0,)
print(zero_zero)
zero_zero.draw(input("what emoji would you like for point 1? "))

hundred_zero = Point(100,0)
print(hundred_zero)
hundred_zero.draw(input("what emoji would you like for point 2? "))

hundred_hundred = Point(100,100)
print(hundred_hundred)
hundred_hundred.draw(input("what emoji would you like for point 3? "))

zero_hundred = Point(0,100)
print(zero_hundred)
zero_hundred.draw(input("what emoji would you like for point 4? "))

#### OPTIONAL extra credit ####
# The `str` function will run the `__str__` method for an object. Use the
# `turtle.write` method and the `str` function to add a label to your point
# when you draw it.


turtle.exitonclick()

