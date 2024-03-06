from account import Account
from transaction import Transaction
from blockchain import Blockchain
import security

# Create accounts
accounts = [
    Account("Anatolii Zavoloka", "1", 0),
    Account("Antonio Banderas", "2", 100),
    Account("Sergio Ramos", "3", 100),
    Account("Paolo Maldini", "4", 200)
  
]

# Generate keys for each account
print('public keys:')
for account in accounts:
    account.public_key, account.private_key = security.generate_keys()
    print(account.public_key)

# Create a blockchain
blockchain = Blockchain()

# Execute transactions
transactions = [
    Transaction(accounts[3], accounts[2], 100),
    Transaction(accounts[2], accounts[1], 100),
    Transaction(accounts[1], accounts[0], 100)
]

# Add transactions to pending transactions in blockchain
for transaction in transactions:
    blockchain.add_transaction(transaction)

# Mine a block with miner reward
miner_reward_address = "miner_reward_address"  # Example miner reward address
blockchain.mine_block(miner_reward_address)

# Update account balances after transactions
for transaction in transactions:
    transaction.execute_transaction()

# Print updated account balances
print("Updated Account Balances:")
for account in accounts:
    print(account)

# Print all transactions involving 100 Tolicoin
print("Transactions involving 100 Tolicoin:")
for transaction in transactions:
    if transaction.amount == 100:
        print(transaction)

# Print the last three transactions in the blockchain
print("\nLast Three Transactions in the Blockchain:")
last_transactions = blockchain.get_last_block().transactions
for transaction in last_transactions:
    print(transaction)

# Print the blockchain
print(blockchain)
