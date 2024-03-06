from account import Account
from transaction import Transaction
from blockchain import Blockchain
import security
from mining import Block  # Importing the Block class from the mining module

def main():
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

    # Check if the blockchain has any blocks before accessing the last block
    if blockchain.chain:
        # Creating a new block and mining it
        new_block = Block(len(blockchain.chain), "01/01/2023", transactions, blockchain.chain[-1].hash)
    else:
        # If blockchain is empty, create a new block with previous_hash as "0"
        new_block = Block(0, "01/01/2023", transactions, "0")
    new_block.mine_block(blockchain.difficulty)

    # Add the mined block to the blockchain
    blockchain.add_block(new_block)

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

if __name__ == "__main__":
    main()
