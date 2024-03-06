import uuid

class Account:
    def __init__(self, owner, account_id, initial_balance):
        self.owner = owner
        self.account_id = account_id
        self.balance = initial_balance
        self.public_key = uuid.uuid4().hex
        self.private_key = uuid.uuid4().hex
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposit: +{amount}")
            return True
        else:
            print("Invalid amount for deposit.")
            return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -{amount}")
            return True
        else:
            print("Insufficient funds or invalid amount for withdrawal.")
            return False

    def get_balance(self):
        return self.balance

    def get_public_key(self):
        return self.public_key

    def get_private_key(self):
        return self.private_key

    def get_transactions(self):
        return self.transactions

    def __str__(self):
        return f"Account {self.account_id}: {self.owner} with balance {self.balance}"

    def print_transaction_history(self):
        print(f"Transaction History for Account {self.account_id}:")
        for transaction in self.transactions:
            print(transaction)
