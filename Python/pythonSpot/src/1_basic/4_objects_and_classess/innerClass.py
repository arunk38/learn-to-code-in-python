"""
    An inner class or nested class is defined completely inside another class.
    There is no limit to number of inner classes
"""


class Human:

    def __init__(self):
        self.name = "Arun"
        self.head = self.Head()
        self.brain = self.Brain()

    class Head:
        def talk(self):
            return "talking...."

    class Brain:
        def think(self):
            return "thinking...."


if __name__ == '__main__':
    arun = Human()
    print(arun.name)
    print(arun.head.talk)
    print(arun.brain.think())