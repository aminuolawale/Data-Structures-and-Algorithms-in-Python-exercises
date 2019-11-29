#ThePredatoryCreditCardclassofSection2.4.1providesaprocess month method that models the completion of a monthly cycle. 
# Modify the class so that once a customer has made ten calls to charge in the current month, each additional call to 
# that function results in an additional $1 surcharge.
from datetime import datetime, timedelta

class CreditCard:
    def __init__(self, customer, bank, acnt, limit):
        self.acnt = acnt
        self.customer = customer
        self.bank = bank
        self.limit = limit
        self.balance = 0
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
        if price + self.balance > self.limit:
            return False
        self.balance += price
        return True
    def make_payment(self, amount):
        self.balance -= amount

class PredatoryCreditCard(CreditCard):
    def __init__(self, customer, bank, acnt, limit, apr):
        super().__init__(self, customer,acnt, limit)
        self.apr = apr
        self.monthly_charge_count = 0
        self.init_time = datetime.utcnow()
        self.MONTH_LENGTH = timedelta(0,4)

    def charge(self, price):
        elapsed_time = datetime.utcnow() - self.init_time
        if elapsed_time > self.MONTH_LENGTH:
            self.monthly_charge_count = 0
        success = super().charge(price)
        if not success:
            self.balance += 5
        if self.monthly_charge_count >=10:
            self.balance+=1
        self.monthly_charge_count+=1
        return success

    def process_month(self):
        if self.balance >0:
            apr_factor = (1+self.apr)**(1/12)
            self.balance *= apr_factor
    
c0 = PredatoryCreditCard('Ammo','a_bank','1111',22000,22)
for _ in range(100):
    slee
    c0.charge(100)
    print(c0.get_balance())