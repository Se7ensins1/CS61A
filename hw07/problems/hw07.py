class Fib():
    """A Fibonacci number."""

    def __init__(self):
        self.value = 0

    def next(self):
        a = Fib()
        if self.value == 0:
            self.previous = 1
        a.value  = self.previous + self.value
        a.previous = self.value
        return a

    def __repr__(self):
        return str(self.value)

class VendingMachine:
    """A vending machine that vends some product for some price."""
    
    def __init__(self, item, price):
        self.item = item
        self.price = price
        self.wallet = 0
        self.stock = 0

    def vend(self):
        if self.stock == 0:
            return 'Machine is out of stock.'
        elif self.wallet < self.price:
            cost = self.price - self.wallet
            return 'You must deposit $' + str(cost) + ' more.'
        elif self.wallet > self.price:
            self.stock -= 1
            change = self.wallet - self.price
            self.wallet = 0
            return 'Here is your ' + self.item + ' and $' + str(change) + ' change.'
        else:
            self.stock -= 1
            self.wallet -= self.price
            return 'Here is your ' + self.item + '.'

    def restock(self, amount):
        self.stock += amount
        return 'Current ' + self.item + ' stock: ' + str(self.stock)

    def deposit(self, amount):
        self.wallet += amount
        if self.stock == 0:
            return 'Machine is out of stock. Here is your $' + str(self.wallet) + "."
        return 'Current balance: $' + str(self.wallet)


class MissManners:
    """A container class that only forward messages that say please."""

    def __init__(self, obj):
        self.obj = obj

    def ask(self, message, *args):
        magic_word = 'please '
        if not message.startswith(magic_word):
            return 'You must learn to say please first.'
        else:
            request = message[7:]
            if hasattr(self.obj, request):
                return getattr(self.obj, request)(*args)
            else:
                return 'Thanks for asking, but I know not how to ' + message[7:] + "."