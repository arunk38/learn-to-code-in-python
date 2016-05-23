class User:
    name = ""

    def __init__(self, name):
        self.name = name

    def printName(self):
        print("Hello " + self.name)


class Programmer(User):
    def __init__(self, name):
        self.name = name

    def doPython(self):
        print("Programming python")


brain = User("Brain")
brain.printName()

diana = Programmer("Diana")
diana.printName()
diana.doPython()

'''
    Brian is an instance of User and can only access the method printName.
    Diana is an instance of Programmer, a class with inheritance from User,
    and can access both the methods in Programmer and User.
'''