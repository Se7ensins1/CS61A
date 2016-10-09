## Lab 6: Trees and Mutable Sequences ##

# Sequences
def map(fn, seq):
    """Applies fn onto each element in seq and returns a list."""
    return list(fn(i) for i in seq)

def filter(pred, seq):
    """Keeps elements in seq only if they satisfy pred."""
    return list(x for x in seq if pred(x))

def reduce(combiner, seq):
    """Combines elements in seq using combiner."""
    total = seq[0]
    for i in seq[1:]:
        total = combiner(total, i)
    return total

# pyTunes
def make_pytunes(username):
    """Return a pyTunes tree as shown in the diagram with USERNAME as the value
    of the root."""
    return tree(username,
                [tree('pop',
                      [tree('justin bieber',
                            [tree('single',
                                  [tree('what do you mean?')])]),
                       tree('2015 popmashup')]),
                 tree('trance',
                      [tree('darude',
                            [tree('sandstorm')])])])

def num_songs(t):
    """Return the number of songs in the pyTunes tree, t."""
    if is_leaf(t):
        return 1
    return 1 + num_songs(branches(t))

def add_song(t, song, category):
    """Returns a new tree with SONG added to CATEGORY. Assume the CATEGORY
    already exists."""
    if root(t) == category:
        return tree(root(t), branches(t) + [tree(song)])
    all_branches = [add_song(b, song, category) for b in branches(t)]
    return tree(root(t), all_branches)
    
# Tree ADT
def tree(root, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [root] + list(branches)

def root(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the entry."""
    print('  ' * indent + str(root(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes."""
    return tree(root(t), [copy_tree(b) for b in branches(t)])
