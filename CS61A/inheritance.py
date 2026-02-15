class Account:
    interest=0.02
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print("Deposit Accepted, Balance is now {}".format(self.balance))
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient Funds")
        else:
            self.balance-=amount
            print("Withdrawal Accepted, Balance is now {}".format(self.balance))
class check_account(Account):
    interest=0.01
    withdraw_fee=1
    def withdraw(self,amount):
        return Account.withdraw(self,amount+self.withdraw_fee)
# check_account inherits from Account and overrides the withdraw method to include a fee. 
# It also has a different interest rate.