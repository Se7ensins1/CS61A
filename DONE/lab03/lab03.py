def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion."""
    min1 = min(a, b)
    max1 = max(a, b)
    if max1 % min1 == 0:
        return min1
    else:
        return gcd(min1, max1 % min1)

def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence."""
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return hailstone(n//2) + 1
    else:
        return hailstone(3 * n + 1) + 1
