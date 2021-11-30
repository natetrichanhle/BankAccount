class BankAccount:

    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate / 100
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('Insufficient funds: Charging a $5 fee')
            self.balance -= 5
        return self
    def display_account_info(self):
        print('Balance', self.balance)
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.int_rate *= self.balance
        return self

p1 = BankAccount(1, 5000)
p2 = BankAccount(4, 2000)
p1.deposit(200).deposit(50).deposit(350).withdraw(200).display_account_info()
p2.deposit(50).deposit(100).withdraw(50).withdraw(25).withdraw(100).withdraw(350).display_account_info()

