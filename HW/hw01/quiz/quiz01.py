"Q1"
def multiple(a, b):
    """Return the smallest number n that is a multiple of both a and b."""
    from fractions import gcd
    return (a*b)//gcd(a,b)

"Q2"
def unique_digits(n):
    """Return the number of unique digits in positive integer n"""
    k=0
    string=""
    while k<10:
        if has_digit(n,k): 
            if string.find(str(k)) > 0:
                k+=1
            else:
                string = string + str(k)
                k+=1
        else:
            k+=1
    return len(string)

   
def has_digit(n,k):
    """Returns true if n has the number k else returns none"""
    while n>0:
        if n%10==k:
            return True
        else:
            n=n//10

    return False

