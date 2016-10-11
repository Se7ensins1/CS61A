## Recursive Objects ##

# Q2
def list_to_link(lst):
    """Takes a Python list and returns a Link with the same elements."""

    if len(lst) == 0:
        return Link.empty
    else:
        return Link(lst[0], list_to_link(lst[1:]))

# Q3
def link_to_list(link):
    """Takes a Link and returns a Python list with the same elements."""

    if link is Link.empty:
        return []
    else:
        return [link.first] + link_to_list(link.rest)

# Q4
def remove_all(link , value):
    """Remove all the nodes containing value. Assume there exists some
    nodes to be removed and the first element is never removed."""
    
    if link == Link.empty or link.rest == Link.empty:
        return
    if link.rest.first == value:
        link.rest = link.rest.rest
        remove_all(link, value)
    else:
        remove_all(link.rest, value)

# Linked List Class
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

    def __len__(self):
        """ Return the number of items in the linked list."""

        return 1 + len(self.rest)

    def __getitem__(self, i):
        """Returning the element found at index i."""

        if i == 0:
            return self.first
        else:
            return self.rest[i-1]

    def __setitem__(self, index, element):
        """Sets the value at the given index to the element"""

        if index == 0:
            self.first = element
        elif self.rest is Link.empty:
            raise IndexError
        else:
            self.rest[index - 1] = element

    def __contains__(self, e):
        return self.first == e or e in self.rest

    def map(self, f):
        self.first = f(self.first)
        if self.rest is not Link.empty:
            self.rest.map(f)

def print_link(link):
    """Print elements of a linked list link."""

    print('<' + helper(link).rstrip() + '>')

def helper(link):
    if link == Link.empty:
        return ''
    elif isinstance(link.first, Link):
        return '<' + helper(link.first).rstrip() + '> ' + helper(link.rest)
    else:
        return str(link.first) +' '+  helper(link.rest)

# Tree Class
class Tree:
    def __init__(self, root, branches=[]):
        for c in branches:
            assert isinstance(c, Tree)
        self.root = root
        self.branches = branches

    def __repr__(self):
        if self.branches:
            branches_str = ', ' + repr(self.branches)
        else:
            branches_str = ''
        return 'Tree({0}{1})'.format(self.root, branches_str)

    def is_leaf(self):
        return not self.branches