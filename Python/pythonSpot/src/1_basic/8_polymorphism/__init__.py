"""
    Polymorphism in python on functions
"""


class Bear(object):
    def sound(self):
        print("Groarrr")


class Dog(object):
    def sound(self):
        print("Woof Woof!!")


def makeSound(animalType):
    animalType.sound()


bearObj = Bear()
dogObj = Dog()

makeSound(bearObj)
makeSound(dogObj)
print("")

'''
    Polymorphism with abstract class (Most commonly used)
    example: If you create an editor you may not know in advance what types of documents a user will open(pdf, word)

        for document in documents:
            print document.name + ": " + document.show()
    To do so, we create an abstract class called document. This class does not have any implementation but define the
    structure that all forms must have. If we define the function show() then both the pdfDocument and wordDocument must
    have the show() function.
'''


class Document:
    def __init__(self, name):
        self.name = name

    def show(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Pdf(Document):
    def show(self):
        return "Show PDF contents"


class Word(Document):
    def show(self):
        return "Show word contents"


documents = [Pdf("doc1"),
             Pdf("doc2"),
             Word("doc3")]

for document in documents:
    print(document.name + ": " + document.show())

print("")
'''
    Another example would be to have an abstract class for Car which holds the structure drive() and stop().
    we define two objs Sportscasr and Truck, both are a form of Car

    pseudo code:
        class Car:
            def drive abstract, no implementation
            def stop abstract, no implementation

        class Sportscar(Car):
            def drive: implementation of sportscar
            def stop:  implementation of sportscar

        class Truck(car):
            def drive: implementation of truck
            def stop: implementation of truck
'''


class Car():
    def __init__(self, name):
        self.name = name

    def drive(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def stop(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Sportscar(Car):
    def drive(self):
        return "Sportscar driving"

    def stop(self):
        return "sportscar breaking!!"


class Truck(Car):
    def drive(self):
        return "Truck driving slowly because heavily loaded"

    def stop(self):
        return "truck breaking!!"


cars = [Truck("Banana Truck"),
        Truck("Orange truck"),
        Sportscar("Z3")]

for car in cars:
    print(car.name + ": " + car.drive())
