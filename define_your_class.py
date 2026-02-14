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
# Example usage:
acct1=Account('Jose',100)
print(acct1.owner)  # Output: Jose
print(acct1.balance)  # Output: 100
acct1.deposit(50)  # Output: Deposit Accepted, Balance is now 150
acct1.withdraw(75)  # Output: Withdrawal Accepted, Balance is now 75
acct1.withdraw(100)  # Output: Insufficient Funds
print(acct1.interest)  # Output: 0.02
print(Account.interest)  # Output: 0.02
acct2=Account('Sally')
acct1.interest=0.03
print(acct1.interest)  # Output: 0.03
print(acct2.interest)  # Output: 0.02
# The above code defines a class named `Account` with an interest rate,
#   an initializer method, and methods for depositing and withdrawing money.
# It also demonstrates how to create instances of the class and use its methods.
print(type(Account.deposit))  # Output: <class 'function'>
print(type(acct1.deposit))  # Output: <class 'method'>