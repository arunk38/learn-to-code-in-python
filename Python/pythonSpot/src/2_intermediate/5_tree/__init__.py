"""
    Python does not have built-in support for trees.
"""


class Tree(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None


root = Tree()
root.data = "root"
root.left = Tree()
root.left.data = "left"
root.right = Tree()
root.right.data = "right"

root.left.left = Tree()
root.left.left.data = "left-left"
root.left.right = Tree()
root.left.right.data = "left-right"

print(root.left.right.data)