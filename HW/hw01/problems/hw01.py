from operator import add, sub

"Q1"
def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs."""
    if b < 0:
        f = sub
    else:
        f = add

    return f(a,b)

"Q2"
def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c."""
    return max(a*a+b*b, b*b+c*c, a*a+c*c)

"Q3"
def largest_factor(n):
    """Return the largest factor of n that is smaller than n."""
    num=0
    k=1
    while k<n:
        if n%k==0:
            num=k
            k+=1
        else:
            k+=1
    return num

"Q4"
def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise."""    
    if condition:
        return true_result
    else:
        return false_result
def with_if_statement():
    """Return 1"""
    if c():
        return t()
    else:
        return f()
def with_if_function():
    """Return anything else"""
    return if_function(c(), t(), f())
def c():
    return False
def t():
    1/0
def f():
    return 1

"Q5"
def hailstone(n):
    """Print the hailstone sequence starting at n and return its length."""
    times = 1
    while n!=1:
        print(n)
        if n%2==0:
            n = n//2
        else:
            n = n*3 + 1
        times = times + 1
    print(n)
    return times
