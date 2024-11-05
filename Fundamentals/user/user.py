class User:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def show_balance(self):
        print(f"User: {self.name}, Balance: ${self.balance}")
        return self

    def transfer(self, recipient, amount):
        self.withdraw(amount)
        recipient.deposit(amount)
        return self

user1 = User("User1", 100)
user2 = User("User2", 200)
user3 = User("User3", 300)

user1.deposit(50).deposit(50).deposit(50).withdraw(100).show_balance()
user2.deposit(100).deposit(100).withdraw(50).withdraw(50).show_balance()
user3.deposit(100).withdraw(50).withdraw(50).withdraw(50).show_balance()

user1.transfer(user3, 50).show_balance()
user3.show_balance()
