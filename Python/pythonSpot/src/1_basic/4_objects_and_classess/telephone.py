class Telephone:
    name = ""
    battery = 0

    def __init__(self, name, battery):
        self.name = name
        self.battery = battery

    def modifyBattery(self, value):
        self.battery = value

    def printBatteryAmount(self):
        print("Model Name: " + self.name)
        print("Current battery amount: " + str(self.battery) + " mAh")

newPhone = Telephone("onePlus2", 3200)
newPhone.printBatteryAmount()
print("")
newPhone.modifyBattery(4000)
newPhone.printBatteryAmount()