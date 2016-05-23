# To disallow direct access to the classes, nest the class within the factory methods
import random


class Shape(object):
    types = []


def factory(type):
    class Circle(Shape):
        def draw(self): print("Circle.draw")

        def erase(self): print("Circle.erase")

    class Square(Shape):
        def draw(self): print("Square.draw")

        def erase(self): print("Square.erase")

    if type == "Circle": return Circle()
    if type == "Square": return Square()
    raise AssertionError("Bad shape creation: " + type)


def shapeNameGen(n):
    for i in range(n):
        yield factory(random.choice(["Circle", "Square"]))


for shape in shapeNameGen(5):
    shape.draw()
    shape.erase()
    print("")