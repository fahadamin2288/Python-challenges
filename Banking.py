from abc import ABC, abstractmethod
from datetime import datetime

class Holder:
    def __init__(self, name):
        self.name = name

class AccountType:
    SAVINGS = 'savings'
    CHECKING = 'checking'

class Date:
    @staticmethod
    def today():
        return datetime.today()

class Account(ABC):
    def __init__(self, holder, balance=0):
        self.holder = holder
        self.balance = balance

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass


class SavingsAccount(Account):
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return amount
        else:
            return "Insufficient balance"

    def deposit(self, amount):
        self.balance += amount
        return amount


class CheckingAccount(Account):
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return amount
        else:
            return "Insufficient balance"

    def deposit(self, amount):
        self.balance += amount
        return amount


holder1 = Holder("Alice")
holder2 = Holder("Bob")
savings_account = SavingsAccount(holder1, 1000)
checking_account = CheckingAccount(holder2, 2000)


print("Savings Account - Initial Balance:", savings_account.balance)
print("Deposit:", savings_account.deposit(500))
print("Withdraw:", savings_account.withdraw(200))
print("Savings Account - Final Balance:", savings_account.balance)

print("\nChecking Account - Initial Balance:", checking_account.balance)
print("Deposit:", checking_account.deposit(1000))
print("Withdraw:", checking_account.withdraw(1500))
print("Checking Account - Final Balance:", checking_account.balance)

print("\nChecking Account - Initial Balance:", checking_account.balance)
print("Deposit:", checking_account.deposit(55000))
print("Withdraw:", checking_account.withdraw(15000))
print("Checking Account - Final Balance:", checking_account.balance)
