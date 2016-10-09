HW_SOURCE_FILE = 'hw04.py'

def g(n):
    """Return the value of G(n), computed recursively."""
    total = 0
    if n<=3:
        return n
    else:
        return g(n-1) + 2 * g(n-2) + 3 * g(n-3)
    
def g_iter(n):
    """Return the value of G(n), computed iteratively."""
    if n <= 3:
        return n
    else:
        for i in range(3,n):
            a, b, c = b, c, (3*a + 2*b + c)
    return c

def pingpong(n):
    """Return the nth element of the ping-pong sequence."""
    def direction(count, n, onestep, index):
        if index == n:
            return count
        else:
            if (index + 1) % 7 == 0 or has_seven(index + 1):
                return direction(count + onestep, n, -onestep, index + 1)
            else:
                return direction(count + onestep, n, onestep, index + 1)
    return direction(0, n, 1, 0)

def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise."""
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)

def count_change(amount):
    """Return the number of ways to make change for amount."""
    coins = []
    x = 1
    while x < amount:
        coins.append(x)
        x=2*x
    ways = [0] * (amount + 1)
    ways[0] = 1
    for coin in coins:
        for j in range(coin, amount + 1):
            ways[j] += ways[j - coin]
    return ways[amount]

###################
# Extra Questions #
###################

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial."""
