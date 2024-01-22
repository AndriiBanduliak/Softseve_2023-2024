class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self._account_number = account_number
        self._account_holder = account_holder
        self._balance = balance

    @property
    def account_holder(self):
        return self._account_holder

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self._balance:
                self._balance -= amount
            else:
                print("Insufficient funds")

    def check_balance(self):
        return self._balance