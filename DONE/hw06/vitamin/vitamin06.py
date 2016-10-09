def make_counter():
    """Return a counter function."""
    dic = {}
    def counter(a):
        if a in dic.keys():
            dic[a] += 1
        else:
            dic[a] = 1
        return dic[a]
    return counter

def make_fib():
    """Returns a function that returns the next Fibonacci number every time it is
    called."""
    index = 0
    lst = [0, 1]
    def next_fib():
        nonlocal index
        lst.append(lst[-1] + lst[-2])
        index += 1
        return lst[index-1]
    return next_fib


class Account:
    """An account has a balance and a holder."""
    interest = 0.02  # A class attribute
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        """Add amount to balance."""
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Subtract amount from balance if funds are available."""
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance

    def time_to_retire(self, amount):
        """Return the number of years until balance would grow to amount."""
        assert self.balance > 0 and amount > 0 and self.interest > 0
        years = 0
        x = self.balance
        while amount > x:
            x *= 1.02
            years += 1
        return years

class FreeChecking(Account):
    """A bank account that charges for withdrawals, but the first two are free!"""
    withdraw_fee = 1
    free_withdrawals = 2
    def withdraw(self, amount):
        self.free_withdrawals -= 1
        if self.free_withdrawals >= 0 and amount <= self.balance:
            self.balance -= amount
        elif self.balance >= (amount + 1):
            self.balance -= (amount + 1)
        else:
            return 'Insufficient funds'
        return self.balance