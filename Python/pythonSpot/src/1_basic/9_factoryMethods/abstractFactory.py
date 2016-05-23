"""
    The Abstract Factory pattern looks like the factory objects we’ve seen previously, with not one but several factory
    methods. Each of the factory methods creates a different kind of object. The idea is that at the point of creation
    of the factory object, you decide how all the objects created by that factory will be used.
"""


class Kitty:
    def interactWith(self, obstacle):
        print("Kitty has encountered a " + obstacle.action())


class KungFuGuy:
    def interactWith(self, obstacle):
        print("KungFuGuy has encountered a " + obstacle.action())


class Puzzle:
    def action(self): return "Puzzle"


class NastyWeapon:
    def action(self): return "NastyWeapon"


# concrete factories
class KittiesAndPuzzels:
    def makeCharacter(self): return Kitty()

    def makeObstacle(self): return Puzzle()


class KillAndDismember:
    def makeCharacter(self): return KungFuGuy()

    def makeObstacle(self): return NastyWeapon()


class GameEnvironment:
    def __init__(self, factory):
        self.factory = factory
        self.p = factory.makeCharacter()
        self.ob = factory.makeObstacle()

    def play(self):
        self.p.interactWith(self.ob)


g1 = GameEnvironment(KittiesAndPuzzels())
g2 = GameEnvironment(KillAndDismember())

g1.play()
g2.play()