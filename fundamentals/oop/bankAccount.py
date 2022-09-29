class BankAccount:

    all_info = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        self.USD = True
        BankAccount.all_info.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance - 5
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        self.balance = self.balance * (1 + self.int_rate)
        return self
    
    # @classmethod
    # def display_all(cls):
    #     print(cls.all_info)

account1 = BankAccount(.05, 100)
account2 = BankAccount(.1, 275)

account1.deposit(50).deposit(75).deposit(130).withdraw(65).yield_interest().display_account_info()

account2.deposit(150).deposit(1000).withdraw(545).withdraw(300).withdraw(50).withdraw(60).yield_interest().display_account_info()

# account1.display_all()