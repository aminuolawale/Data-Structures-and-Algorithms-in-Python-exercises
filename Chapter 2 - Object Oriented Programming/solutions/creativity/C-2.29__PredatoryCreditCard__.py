# Modify the PredatoryCreditCard class from Section 2.4.1 so that a customer is assigned a minimum monthly payment, as a 
# percentage of the balance, and so that a late fee is assessed if the customer does not subsequently pay that minimum 
# amount before the next monthly cycle

from tryouts.creditcard import CreditCard
from datetime import datetime, timedelta
class PredatoryCreditCard(CreditCard):
    def __init__(self, customer, bank, acnt, limit, apr):
        super().__init__(self, customer,acnt, limit)
        self.apr = apr
        self.monthly_charge_count = 0
        self.init_time = datetime.utcnow()

    def charge(self, price):
        success = super().charge(price)
        if not success:
            self.balance += 5
        if self.monthly_charge_count >=10:
            self.balance += 1
        self.monthly_charge_count+=1
        return success
    def process_month(self):
        if self.balance >0:
            apr_factor = (1+self.apr)**(1/12)
            self.balance *= apr_factor
    
c0 = PredatoryCreditCard('Ammo','a_bank','1111',22000,22)
c0.charge(23001)
print(c0.get_balance())