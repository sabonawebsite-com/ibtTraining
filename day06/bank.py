# Observer Pattern
class SMSAlert:
    def update(self, message):
        print(f"SMS Alert: {message}")


# Base Account Class
class Account:
    def init(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)

    def deposit(self, amount):
        self.balance += amount
        self.notify(f"{self.owner} deposited ${amount}. Balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.notify(f"{self.owner} withdrew ${amount}. Balance: ${self.balance}")
        else:
            print("Insufficient funds.")

    def display(self):
        print(f"{self.owner} Balance: ${self.balance}")


# Savings Account
class SavingsAccount(Account):
    def init(self, owner, balance=0):
        super().init(owner, balance)


# Checking Account
class CheckingAccount(Account):
    def init(self, owner, balance=0):
        super().init(owner, balance)


# Factory Pattern
class AccountFactory:
    @staticmethod
    def create(kind, owner, balance=0):
        if kind.lower() == "savings":
            return SavingsAccount(owner, balance)
        elif kind.lower() == "checking":
            return CheckingAccount(owner, balance)
        else:
            raise ValueError("Invalid account type")


# Main Program
if __name__ == "main":
    alert = SMSAlert()

    account1 = AccountFactory.create("savings", "Alice", 1000)
    account2 = AccountFactory.create("checking", "Bob", 500)

    account1.subscribe(alert)
    account2.subscribe(alert)

    account1.deposit(200)
    account1.withdraw(150)

    account2.deposit(100)
    account2.withdraw(700)

    account1.display()
    account2.display()