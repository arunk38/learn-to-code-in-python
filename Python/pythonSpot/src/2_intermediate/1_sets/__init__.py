"""
    A set in python is a collection of objects, different from lists and tuples.
    Modeled after set in mathematics
"""

# Multiple occurrences of same item are removed
x = set(["Postcard", "Radio", "Telegram", "Postcard"])
print(x)

# remove elements
x.remove("Radio")
print(x)

# add elements
x.add("Telephone")
print(x)

# clear elements
x.clear()
print(x)

# difference between two 1_sets
x = set(["Postcard", "Radio", "Telegram", "Postcard"])
y = {"Radio", "Telegram", "Mobile"}
print(x.difference(y))
print(y.difference(x))

# super-set
print(x.issuperset(y))

# intersection
print(x.intersection(y))

