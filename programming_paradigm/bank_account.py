class BankAccount:
    def __init__(self, initial_balance=0.0):
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited: ${amount}")

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew: ${amount}")
            return True
        print("Insufficient funds")
        return False

    def display_balance(self):
        print(f"Current Balance: $100.00")

    