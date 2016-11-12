def countdown(n):
    """Write a generator function that counts down to 0"""
    while n >= 0:
        yield n
        n-=1

def trap(s, k):
    """Return a generator that yields the first K values in iterable S,
    but raises a ValueError exception if any more values are requested.
    """
    assert len(s) >= k
    while k > 0:
        yield s[0]
        k-=1
        s = s[1::]
    raise ValueError

def repeated(t, k):
    """Return the first value in iterator T that appears K times in a row.

    >>> s = [3, 2, 1, 2, 1, 4, 4, 5, 5, 5]
    >>> repeated(trap(s, 7), 2)
    4
    >>> repeated(trap(s, 10), 3)
    5
    >>> print(repeated([4, None, None, None], 3))
    None
    """
    assert k > 1

    if t != iter(t):
        t = iter(t)
    first = next(t)
    while k > 0:
        second = next(t)
        if first == second:
            k -= 1
            if k == 1:
                return first
        else:
            first = second


def hailstone(n):
    """Write a generator that outputs the hailstone sequence from homework 1."""
    while n > 1:
        yield n
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    yield 1