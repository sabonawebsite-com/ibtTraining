class Account:
    def __init__(self, owner, balance=25):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount


class SavingsAccount(Account):
    def __init__(self, owner, balance=0, rate=0.05):
        super().__init__(owner, balance)
        self.rate = rate

    def add_interest(self):
        self.deposit(self.balance * self.rate)


almaz = SavingsAccount("Almaz", 1500)
boy = SavingsAccount("sabona", 1000)

almaz.deposit(500)
boy.deposit(300)

print(almaz.balance)
print(boy.balance)

accounts = [
    Account("Hanna", 1500), 
    SavingsAccount("Almaz", 1500), 
 
] 
for acc in accounts: 
    acc.statement() 