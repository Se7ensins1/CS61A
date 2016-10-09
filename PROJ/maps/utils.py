"""Utilities for Maps"""

from math import sqrt
from random import sample

# Rename the built-in zip (http://docs.python.org/3/library/functions.html#zip)
_zip = zip

def map_and_filter(s, map_fn, filter_fn):
    """Returns a new list containing the results of calling map_fn on each
    element of sequence s for which filter_fn returns a true value."""
    return list(map_fn(x) for x in s if filter_fn(x))

def key_of_min_value(d):
    """Returns the key in a dict d that corresponds to the minimum value of d."""
    return list(i for i in d.keys() if d[i] == min(d.values()))[0]

def zip(*sequences):
    """Returns a list of lists, where the i-th list contains the i-th
    element from each of the argument sequences."""
    return list(map(list, _zip(*sequences)))

def enumerate(s, start=0):
    """Returns a list of lists, where the i-th list contains i+start and
    the i-th element of s."""
    return zip(range(start, start + len(s)), s)

def distance(pos1, pos2):
    """Returns the Euclidean distance between pos1 and pos2, which are pairs."""
    return sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)

def mean(s):
    """Returns the arithmetic mean[ of a sequence of numbers s."""
    assert len(s) > 0, 'cannot find mean of empty sequence'
    return sum(s) / len(s)
