import hashlib
import datetime
from transaction import Transaction
class Block:
    def __init__(self, transactions, previous_hash=''):
        self.timestamp = datetime.datetime.now()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        return hashlib.sha256((str(self.timestamp) + str(self.transactions) + str(self.previous_hash) + str(self.nonce)).encode()).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print("Block mined:", self.hash)


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4  # Adjust the difficulty as per your requirement
        self.pending_transactions = []

    def create_genesis_block(self):
        return Block([], "0")

    def get_last_block(self):
        return self.chain[-1]

    def add_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def mine_block(self, miner_reward_address):
        block = Block(self.pending_transactions, self.get_last_block().hash)
        block.mine_block(self.difficulty)
        self.chain.append(block)
        self.pending_transactions = [
            Transaction(None, miner_reward_address, miner_reward) for miner_reward in [10]  # Example miner reward
        ]

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def __str__(self):
        chain_str = "\n".join([f"Block {i}: {block.hash}" for i, block in enumerate(self.chain)])
        return f"Blockchain:\n{chain_str}"
