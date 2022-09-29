class BankAccount:

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            self.balance = self.balance - 5
            print("Insufficient funds: Charging a $5 fee")

class User:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.checking = BankAccount(.04, 0)
        self.savings = BankAccount(.07, 0)

    def make_deposit(self, account, amount):
        if account == "checking":
            self.checking.deposit(amount)
        elif account == "savings":
            self.savings.deposit(amount)
        return self

    def make_withdrawal(self, account, amount):
        if account == "checking":
            self.checking.withdraw(amount)
        elif account == "savings":
            self.savings.withdraw(amount)
        return self

    def display_user_balance(self, account):
        if account == "checking":
            print(f"User: {self.first_name}, Checking Balance: {self.checking.balance}")
        elif account == "savings":
            print(f"User: {self.first_name}, Savings Balance {self.savings.balance}")
        return self

    def transfer_money(self, account, amount, other_user):
        if account == "checking":
            self.checking.withdraw(amount)
            other_user.checking.deposit(amount)
        elif account == "savings":
            self.savings.withdraw(amount)
            other_user.savings.deposit(amount)
        return self

user1 = User("Karsten", "Wersland", 22)
user2 = User("Sam", "Wersland", 24)
user3 = User("Jackson", "Paulo", 19)

user1.make_deposit("checking", 1000).make_deposit("savings", 1200).transfer_money("checking", 500, user2).display_user_balance("checking").display_user_balance("savings")
user2.make_deposit("savings", 2300).transfer_money("savings", 1200, user3).display_user_balance("checking").display_user_balance("savings")
user3.make_deposit("checking", 500).make_withdrawal("checking", 1000).display_user_balance("checking").display_user_balance("savings")