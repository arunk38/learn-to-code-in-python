class Car:
    __maxspeed = 0  # Python interpreter renames these to _<classname>__<variable name>
    __name = ""  # i.e __maxspeed will be something like this... _Car__maxspeed

    # for more info print <class object>.__dict__, read doc for more info

    def __init__(self):
        self.__maxspeed = 200
        self.__name = "SuperCar"

    def drive(self):
        print("driving. maxspeed " + str(self.__maxspeed))

    def setMaxSpeed(self, speed):
        self.__maxspeed = speed


redCar = Car()
redCar.drive()
redCar.setMaxSpeed(230)
redCar.drive()
redCar.__maxspeed = 10  # will not change variable because its private
redCar.drive()
redCar._Car__maxspeed = 300 # will change the variable
redCar.drive()