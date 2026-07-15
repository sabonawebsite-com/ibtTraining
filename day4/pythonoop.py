class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance!")

    def statement(self):
        print(f"Account: {self.owner} | Balance: ${self.balance:.2f}")


class SavingsAccount(Account):
    def init(self, owner, balance, rate):
        super().init(owner, balance)
        self.rate = rate

    def add_interest(self):
        self.balance += self.balance * self.rate

    def statement(self):
        print(f"Savings Account: {self.owner} | Balance: ${self.balance:.2f}")


class CurrentAccount(Account):
    def init(self, owner, balance, overdraft):
        super().init(owner, balance)
        self.overdraft = overdraft

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft:
            self.balance -= amount
        else:
            print("Overdraft limit exceeded!")

    def statement(self):
        print(f"Current Account: {self.owner} | Balance: ${self.balance:.2f}")


# Create objects
acc1 = Account("Tola", 100000)

acc2 = SavingsAccount("Chaltu", 20000, 0.05)
acc2.add_interest()

acc3 = CurrentAccount("Getuu", 500, 300)
acc3.withdraw(600)

# Polymorphic loop
accounts = [acc1, acc2, acc3]

for account in accounts:
    account.statement()