from random import *

print (random())     # Generate a pseudo-random_exp number between 0 and 1.

print(randint(1, 100)) # Generate a random_exp number between 1 and 100.

print (uniform(1, 1120)) # Generate random_exp floating point number between 1 and 10.

# Fun with lists

items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

shuffle(items)
print (items)

x = sample(items, 1) # Pick a random_exp item from the list
print (x[0])

y = sample(items, 4) # Pick 4 random_exp items from the list
print (y)
print (y[2])
