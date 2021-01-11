class User:
    def __init__(self):
        self.balance= 0
    def make_deposit(self, amount):
        self.balance = self.balance + amount
        print(self.balance)
    def make_withdrawl(self,amount):
        self.balance = self.balance - amount
        print(self.balance)
        return self
    #def print_balance(self):
        return self.balance
account = User()
account.make_deposit(100)
account.make_withdrawl(50)