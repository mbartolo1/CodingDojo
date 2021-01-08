class BankAccount: 
    def __init__(self, int_rate, balance):
        self.balance = balance
        self.int_rate = int_rate
    def withdrawl(self,amount):
        self.balance -= amount
        print (self.balance)
        return self
    def deposit(self,amount):
        self.balance += amount
        print(self.balance)
        return self
    def interest_rate(self):
        if self.balance > 1:
            self.balance += self.int_rate * self.balance
            print(self.balance)
        return self
    def display_account_info(self,balance):
        print(self.balance)
        print(self.int_race)
user1= BankAccount( balance = 500, int_rate=0.02)
user2= BankAccount(balance=200, int_rate=0.02)
user1.deposit(100).deposit(400).deposit(300).withdrawl(100).interest_rate()
user2.deposit(300).withdrawl(100).withdrawl(100).withdrawl(100).withdrawl(100).interest_rate()