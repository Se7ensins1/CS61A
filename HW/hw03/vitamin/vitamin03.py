HW_SOURCE_FILE = 'vitamin03.py'

def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise."""
    while k > 0:
        if k % 10 == 7:
            return True
        else:
            k = k // 10
    return False

def summation(n, term):
    """Return the sum of the first n terms in the sequence defined by term.
    Implement using recursion!

    >>> summation(5, lambda x: x * x * x) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
    225
    >>> summation(9, lambda x: x + 1) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    54
    >>> summation(5, lambda x: 2**x) # 2^1 + 2^2 + 2^3 + 2^4 + 2^5
    62
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'summation',
    ...       ['While', 'For'])
    True
    """
    assert n >= 1
    if n==1:
        return term(n)
    else:
        return term(n) + summation(n-1, term)
