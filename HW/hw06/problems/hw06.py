###########
# Mobiles #
###########

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

def mobile(left, right):
    """Construct a mobile from a left side and a right side."""
    return tree(None, [left, right])

def sides(m):
    """Select the sides of a mobile."""
    return branches(m)

def side(length, mobile_or_weight):
    """Construct a side: a length of rod with a mobile or weight at the end."""
    return tree(length, [mobile_or_weight])

def length(s):
    """Select the length of a side."""
    return root(s)

def end(s):
    """Select the mobile or weight hanging at the end of a side."""
    return branches(s)[0]

def weight(size):
    """Construct a weight of some size."""
    assert size > 0
    return tree(size)

def size(w):
    """Select the size of a weight."""
    return root(w)

def is_weight(w):
    """Whether w is a weight, not a mobile."""
    return bool(root(w))

def examples():
    t = mobile(side(1, weight(2)),
               side(2, weight(1)))
    u = mobile(side(5, weight(1)),
               side(1, mobile(side(2, weight(3)),
                              side(3, weight(2)))))
    v = mobile(side(4, t), side(2, u))
    return (t, u, v)


def total_weight(m):
    """Return the total weight of m, a weight or mobile."""
    if is_weight(m):
        return size(m)
    else:
        return sum([total_weight(end(s)) for s in sides(m)])

def balanced(m):
    """Return whether m is balanced.

    >>> t, u, v = examples()
    >>> balanced(t)
    True
    >>> balanced(v)
    True
    >>> w = mobile(side(3, t), side(2, u))
    >>> balanced(w)
    False
    >>> balanced(mobile(side(1, v), side(1, w)))
    False
    >>> balanced(mobile(side(1, w), side(1, v)))
    False
    """
    result = []
    for s in sides(m):
        if is_weight(end(s)):
            result.append(size(end(s)) * length(s))
        elif balanced(end(s)):
            result.append(total_weight(end(s)) * length(s))
        else:
            result.append(False)
    if result[0] == result[1] and False not in result:
        return True
    else:
        return False


def with_totals(m):
    """Return a mobile with total weights stored as the root of each mobile."""
    rt = 0
    if is_weight(m):
        return weight(size(m))
    if root(m) != None:
        rt = root(m)
    else:
        rt = total_weight(m)
    return tree(rt, [side(length(s), with_totals(end(s))) for s in sides(m)])

############
# Mutation #
############

def make_withdraw(balance, password):
    """Return a password-protected withdraw function."""
    lst = []
    num_attempts = 3
    def withdraw(amount, attempt):
        nonlocal balance 
        if num_attempts <= 0:
            return "Your account is locked. Attempts: {0}". format(lst)
        elif attempt != password:
            num_attempts -= 1   
            lst.append(attempt)
            return 'Incorrect password'  
        elif amount > balance:
            return 'Insufficient funds'
        else:
            balance -= amount
            return balance
    return withdraw

def make_joint(withdraw, old_password, new_password):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw."""
    x = withdraw(0, old_password)
    if type(x) == str:
        return x
    def withdrawal(amount, attempt):
        if attempt == new_password:
            attempt = old_password
        return withdraw(amount, attempt)
    return withdrawal
