"""
    The static factory( ) method in the previous example forces all the creation operations to be focused in one spot,
    so that’s the only place you need to change the code. This is certainly a reasonable solution, as it throws a box
    around the process of creating objects. However, the Design Patterns book emphasizes that the reason for the Factory
    Method pattern is so that different types of factories can be subclassed from the basic factory
"""

from __future__ import generators
import random


class ShapeFactory:
    factories = {}

    @staticmethod
    def addFactory(id, shapeFactory):
        ShapeFactory.factories.put[id]  =shapeFactory

    @staticmethod
    def createShape(id):
        if id not in ShapeFactory.factories:
            ShapeFactory.factories[id] = eval(id + '.Factory()')
        return ShapeFactory.factories[id].create()


class Shape(object): pass


class Circle(Shape):
    def draw(self): print("Circle.draw")

    def erase(self): print("Circle.erase")

    class Factory:
        def create(self): return Circle()


class Square(Shape):
    def draw(self): print("Square.draw")

    def erase(self): print("Square.erase")

    class Factory:
        def create(self): return Square()


def shapeNameGen(n):
    types = Shape.__subclasses__()
    for i in range(n):
        yield random.choice(types).__name__

shapes = \
    [ ShapeFactory.createShape(i) for i in shapeNameGen(5)]

for shape in shapes:
    shape.draw()
    shape.erase()
    print("")