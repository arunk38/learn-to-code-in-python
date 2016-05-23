class CoffeeMachine:
    name = ""
    beans = 0
    __water = 0

    def __init__(self, name, beans, water):
        self.name = name
        self.beans = beans
        self.__water = water

    def addBean(self):
        self.beans += 1

    def removeBeans(self):
        self.beans -= 1

    def addWater (self):
        self.__water += 1

    def removeWater(self):
        self.__water -= 1

    def printState (self):
        print("Name : " + self.name)
        print("Beans : " + str(self.beans))
        print("Water : " + str(self.__water))

pythonBean = CoffeeMachine("pyBean", 12, 32)
pythonBean.printState()
print("")
pythonBean.addBean()
pythonBean.printState()
print("")
pythonBean._CoffeeMachine__water = 100
print(pythonBean.__dict__)
pythonBean.printState()
