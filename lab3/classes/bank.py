class Account:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
        self.deposit=0
    def withdraw(self):
        print("How much do you want to withdraw")
        money=int(input())
        if money>self.balance:
            print("Lack of funds")
        else:
            self.balance-=money
            print(self.owner,"'s balance now:", self.balance)
    def deposit_oper(self):
        print("How much money do you want to put in deposit")
        money=int(input())
        if money>self.balance:
            print("Lack of funds")
        else:
            self.balance-=money
            self.deposit+=money
            print(self.owner,"'s deposit:", self.deposit)
owner=input()
balance=int(input())
bank=Account(owner,balance)
bank.withdraw()
bank.deposit_oper()
