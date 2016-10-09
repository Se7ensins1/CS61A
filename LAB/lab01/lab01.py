"""Lab 1: Expressions and Control Structures"""

"Q3"
def repeated(f, n, x):
    """Returns the result of composing f n times on x."""
    if f==square:
        a=x*x
        while n>1:
            a = a*a
            n-=1
        return a
    elif f==opposite:
        if n%2==0:
            return  x
        elif x:
            return False
        else:
            return True
    else:
        return 1
def square(x):
    return x*x
def opposite(b):
    return not b

"Q4"
def sum_digits(n):
    """Sum all the digits of n."""
    total=0
    while n>0:
        total+=n%10
        n=n//10
    return total

"Q5"
def double_eights(n):
    """Return true if n has two eights in a row."""
    a=n%10
    while n>9:
        b=(n//10)%10
        if (a==8 & b==8):
            return True
        else:
            a=b
            n=n//10
    return False
