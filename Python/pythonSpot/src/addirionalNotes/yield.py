"""
    To understand what yield does, you must understand what generators are. And before generators come iterables.

    Iterables:
        When you create a list, you can read its items one by one. Reading its items one by one is called iteration.

    Generators:
        Generators are iterators, but you can only iterate over them once. It's because they do not store all the values
        in memory, they generate the values on the fly.

    Yield:
        Yield is a keyword that is used like return, except the function will return a generator.

        def createGenerator():
             mylist = range(3)
             for i in mylist:
                yield i*i

        mygenerator = createGenerator() # create a generator
        print(mygenerator) # mygenerator is an object!
        <generator object createGenerator at 0xb7555c34>
        for i in mygenerator:
            print(i)
        0
        1
        4

    Here it's a useless example, but it's handy when you know your function will return a huge set of values that you
    will only need to read once.

    To master yield, you must understand that when you call the function, the code you have written in the function body
    does not run. The function only returns the generator object, this is a bit tricky :-)

    Then, your code will be run each time the for uses the generator.

    Now the hard part:

    The first time the for calls the generator object created from your function, it will run the code in your function
    from the beginning until it hits yield, then it'll return the first value of the loop. Then, each other call will
    run the loop you have written in the function one more time, and return the next value, until there is no value to
    return.

    The generator is considered empty once the function runs but does not hit yield anymore. It can be because the loop
    had come to an end, or because you do not satisfy a "if/else" anymore.
"""
import math


def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False


def get_primes(number):
    while True:
        if is_prime(number):
            yield number # code freezes here and returns to caller until next call and resumes from here
        number += 1


def solve_number_10():
    # She *is* working on Project Euler #10, I knew it!
    total = 2
    for next_prime in get_primes(3):
        if next_prime < 2000000:
            total += next_prime
        else:
            print(total)
            return

solve_number_10()