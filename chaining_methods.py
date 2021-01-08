class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def withdrawl(self,amount):
        self.balance -= amount
        print (self.name,self.balance)
        return self
    def make_deposit(self, amount):
        self.balance += amount
        amount = int 
        print (f'{self.name}, {self.balance}')
        return self
    def display_user_balance(self):
        print (self.balance)
user1 = User(name = "mario", balance = 500)
user1.make_deposit(100).withdrawl(200).display_user_balance()
