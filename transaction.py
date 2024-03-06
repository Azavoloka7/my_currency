# transaction.py

import hashlib

class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.transaction_hash = self.calculate_hash()

    def execute_transaction(self):
        if self.sender.withdraw(self.amount):
            self.receiver.deposit(self.amount)
            return True
        else:
            print("Transaction failed: Insufficient balance.")
            return False

    def calculate_hash(self):
        data = str(self.sender) + str(self.receiver) + str(self.amount)
        return hashlib.sha256(data.encode()).hexdigest()

    def __str__(self):
        return f"Transaction: {self.sender.owner} sent {self.amount} to {self.receiver.owner}"
