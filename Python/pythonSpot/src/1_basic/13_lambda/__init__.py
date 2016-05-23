"""
    Lambda are anonymous functions
    ex:
        f = lambda x : 2 * x
        print f(3)
"""

# map function
import functools

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squaredList = list(map(lambda x: x*x, list1))
print(squaredList)


# filter function
newList = list(filter(lambda x: x%2 == 0, list1))
print(newList)
