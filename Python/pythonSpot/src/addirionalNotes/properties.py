"""
    In Python, property() is a built-in function that creates and returns a property object. The signature of this
    function is:
        property(fget=None, fset=None, fdel=None, doc=None)

    where, fget is function to get value of the attribute, fset is function to set value of the attribute, fdel is
    function to delete the attribute and doc is a string (like a comment). As seen from the implementation, these
    function arguments are optional.
"""


class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property  # Adding property on temperature variable
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter  # setting up setter for temperature variable
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value


c = Celsius(37)
print(c.temperature)
print(c.to_fahrenheit())
