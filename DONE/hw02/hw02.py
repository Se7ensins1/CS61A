HW_SOURCE_FILE = 'hw02.py'

def square(x):
    return x * x

def triple(x):
    return 3 * x

def identity(x):
    return x

def increment(x):
    return x + 1

def product(n, term):
    """Return the product of the first n terms in a sequence."""
    num=1
    while n>0:
        if term == identity:
            num = num * identity(n)
        elif term == square:
            num = num * square(n)
        n-=1
    return num

# The identity function, defined using a lambda expression!
identity = lambda k: k

def factorial(n):
    """Return n factorial for n >= 0 by calling product."""
    return product(n, identity)

def make_adder(n):
    """Return a function that takes an argument K and returns N + K."""    
    return lambda k: k+n

