class Human:

    def sayHello(self, name=None):
        if name is not None:
            print("Hello " + name)
        else:
            print("Hello")

# create instance
obj = Human()

# call tha method
obj.sayHello()
obj.sayHello("Arun")