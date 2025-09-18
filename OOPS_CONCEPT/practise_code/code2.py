class Account:
    def __init__(self,balance,account_no):
        self.balance=balance
        self.account_no=account_no
    def debit(self,debit):
        self.balance-=debit
        print("Your account is debited from:",self.balance)
    def credit(self,credit):
        self.balance+=credit
        print("Your account is credited from:",self.balance)
        print("Your total balance is ",self.balance)
acc1=Account(10000,"A123")
acc1.debit(12000)
acc1.credit(3000)
