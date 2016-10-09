class Link:
    """A linked list."""
    
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is Link.empty:
            return 'Link({})'.format(self.first)
        else:
            return 'Link({}, {})'.format(self.first, repr(self.rest))

def digits(n):
    """Return the digits of n as a linked list."""

    s = Link.empty
    while n > 0:
        n, last = n // 10, n % 10
        s = Link(last, s)
    return s