class BankAccount:

    def __init__(self, name, account_number, balance):
        self.name=name
        self.account_number=account_number
        self.balance=balance

    def replenishment(self, amount):
        self.balance += amount

    def withdrawal(self, amount):
        self.balance-=amount

bankAccount1=BankAccount("Эльвира", 5421222222211125, 5000000)
print(bankAccount1.balance)
bankAccount1.replenishment(50000)
print(bankAccount1.balance)
bankAccount1.withdrawal(600000)
print(bankAccount1.balance)