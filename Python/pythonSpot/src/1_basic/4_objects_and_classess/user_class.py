class User:
    name = ""

    def __init__(self, name):
        self.name = name

    def sayHello(self):
        print("Hello my name is " + self.name)


# Create virtual objects
arun = User("Arun")
david = User("David")

# Call methods to owned virtual objects
arun.sayHello()
david.sayHello()
