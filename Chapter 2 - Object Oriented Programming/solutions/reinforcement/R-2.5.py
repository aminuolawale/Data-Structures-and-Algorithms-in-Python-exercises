#Use the techniques of Section 1.7 to revise the charge and make payment methods of the CreditCard class to ensure that the caller sends a 
# number as a parameter.

# section 1.7 was on Exception Handling

class CreditCard:
    def __init__(self, customer, bank, acnt, limit):
        self.acnt = acnt
        self.customer = customer
        self.bank = bank
        self.limit = limit
        self.balance = 0
    @staticmethod
    def is_numeric(value):
        return type(value) == type(1) or type(value) == type(1.0)
    def get_customer(self):
        return self.customer
    def get_bank(self):
        return self.bank
    def get_account(self):
        return self.acnt
    def get_limit(self):
        return self.limit
    def get_balance(self):
        return self.balance
    def charge(self, price):
        if not self.is_numeric(price):
            raise TypeError('price must be int or float')
        if price + self.balance > self.limit:
            return False
        self.balance += price
        return True
    def make_payment(self, amount):
        if not self.is_numeric(amount):
            raise TypeError('price must be int or float')
        self.balance -= amount
        
if __name__ == '__main__':
    card = CreditCard('AMinu Mohammed','Fbank','121231332',200)
    card.charge('eeee')
