import csv
from typing import Union

class BankAccount:
    def __init__(self, bank: 'Bank', name: str, balance: float = 0):
        self.bank = bank
        # Account name is case-insensitive
        self.name = name.upper()
        # Minimal accounting precision is cent
        self.balance_cents: int = round(balance * 100)

    @property
    def balance(self):
        return self.balance_cents / 100

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance_cents += round(amount * 100)

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.balance:
            raise ValueError("Overdraft is not allowed")
        self.balance_cents -= round(amount * 100)

    def transfer(self, other: Union['BankAccount', str], amount: float):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        if isinstance(other, str):
            other = self.bank.get_account(other)
        self.withdraw(amount)
        other.deposit(amount)

    def __str__(self):
        return f"{self.name} has {self.balance} dollars"

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name: str, balance: float = 0):
        name = name.upper()
        if name in self.accounts:
            raise ValueError("Account already exists")
        self.accounts[name] = BankAccount(self, name, balance)
        return self.accounts[name]

    def get_account(self, name: str):
        return self.accounts[name.upper()]

    def save_to_csv(self, filename: str):
        with open(filename, "w") as f:
            writer = csv.writer(f)
            writer.writerow(["name", "balance"])
            for name, account in self.accounts.items():
                writer.writerow([name, account.balance])

    def load_from_csv(self, filename: str):
        with open(filename, "r") as f:
            reader = csv.reader(f)
            next(reader)  # Skip header row
            for name, balance in reader:
                self.create_account(name, float(balance))


