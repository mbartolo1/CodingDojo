class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def withdrawl(self,amount):
        self.balance -= amount
        print (self.name,self.balance)
        return self
    def deposit(self, amount):
        self.balance += amount
        print (f'{self.name},{self.balance}')
        return self
user1 = User(name = "mario", balance = 500)
user2 = User(name = "joe", balance = 800)
user3 = User(name = "moe", balance = 400)
user2.withdrawl(200)
user1.withdrawl(150)
user3.withdrawl(200)
user1.deposit(200)
user1.deposit(300)
user2.deposit(300)
user2.deposit(400)
user2.withdrawl(500)
user3.deposit(300)
user3.withdrawl(400)
user3.withdrawl(100)

