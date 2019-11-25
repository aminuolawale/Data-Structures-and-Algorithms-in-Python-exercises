from creditcard import CreditCard

class PredatoryCreditCard(CreditCard):
    def __init__(self, customer, bank, acnt, limit, apr):
        super().__init__(self, customer,acnt, limit)
        self.apr = apr

    def charge(self, price):
        success = super().charge(price)
        if not success:
            self.balance += 5
        return success
    def process_month(self):
        if self.balance >0:
            apr_factor = (1+self.apr)**(1/12)
            self.balance *= apr_factor
    
c0 = PredatoryCreditCard('Ammo','a_bank','1111',22000,22)
c0.charge(23001)
print(c0.get_balance())

